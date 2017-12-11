from __future__ import division  # py3 "true division"

import logging

try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty  # noqa:F401

from numpy import zeros, dtype, float32 as REAL, fromstring, ascontiguousarray

from gensim import utils  # utility fnc for pickling, common scipy operations etc
from gensim.keyedvectors import Vocab
from six.moves import xrange


logger = logging.getLogger(__name__)


def load_word2vec_format(cls, fname, fvocab=None, binary=False, encoding='utf8', unicode_errors='strict',
                         limit=None, datatype=REAL):
    """
    Load the input-hidden weight matrix from the original C word2vec-tool format.

    Note that the information stored in the file is incomplete (the binary tree is missing),
    so while you can query for word similarity etc., you cannot continue training
    with a model loaded this way.

    `binary` is a boolean indicating whether the data is in binary word2vec format.
    `norm_only` is a boolean indicating whether to only store normalised word2vec vectors in memory.
    Word counts are read from `fvocab` filename, if set (this is the file generated
    by `-save-vocab` flag of the original C tool).

    If you trained the C model using non-utf8 encoding for words, specify that
    encoding in `encoding`.

    `unicode_errors`, default 'strict', is a string suitable to be passed as the `errors`
    argument to the unicode() (Python 2.x) or str() (Python 3.x) function. If your source
    file may include word tokens truncated in the middle of a multibyte unicode character
    (as is common from the original word2vec.c tool), 'ignore' or 'replace' may help.

    `limit` sets a maximum number of word-vectors to read from the file. The default,
    None, means read all.

    `datatype` (experimental) can coerce dimensions to a non-default float type (such
    as np.float16) to save memory. (Such types may result in much slower bulk operations
    or incompatibility with optimized routines.)

    """
    counts = None
    if fvocab is not None:
        logger.info("loading word counts from %s", fvocab)
        counts = {}
        with utils.smart_open(fvocab) as fin:
            for line in fin:
                word, count = utils.to_unicode(line).strip().split()
                counts[word] = int(count)

    logger.info("loading projection weights from %s", fname)
    with utils.smart_open(fname) as fin:
        header = utils.to_unicode(fin.readline(), encoding=encoding)
        vocab_size, vector_size = (int(x) for x in header.split())  # throws for invalid file format
        if limit:
            vocab_size = min(vocab_size, limit)
        result = cls()
        result.vector_size = vector_size
        result.syn0 = zeros((vocab_size, vector_size), dtype=datatype)

        def add_word(word, weights):
            word_id = len(result.vocab)
            if word in result.vocab:
                logger.warning("duplicate word '%s' in %s, ignoring all but first", word, fname)
                return
            if counts is None:
                # most common scenario: no vocab file given. just make up some bogus counts, in descending order
                result.vocab[word] = Vocab(index=word_id, count=vocab_size - word_id)
            elif word in counts:
                # use count from the vocab file
                result.vocab[word] = Vocab(index=word_id, count=counts[word])
            else:
                # vocab file given, but word is missing -- set count to None (TODO: or raise?)
                logger.warning("vocabulary file is incomplete: '%s' is missing", word)
                result.vocab[word] = Vocab(index=word_id, count=None)
            result.syn0[word_id] = weights
            result.index2word.append(word)

        if binary:
            binary_len = dtype(REAL).itemsize * vector_size
            for _ in xrange(vocab_size):
                # mixed text and binary: read text first, then binary
                word = []
                while True:
                    ch = fin.read(1)
                    if ch == b' ':
                        break
                    if ch == b'':
                        raise EOFError("unexpected end of input; is count incorrect or file otherwise damaged?")
                    if ch != b'\n':  # ignore newlines in front of words (some binary files have)
                        word.append(ch)
                word = utils.to_unicode(b''.join(word), encoding=encoding, errors=unicode_errors)
                weights = fromstring(fin.read(binary_len), dtype=REAL)
                add_word(word, weights)
        else:
            for line_no in xrange(vocab_size):
                line = fin.readline()
                if line == b'':
                    raise EOFError("unexpected end of input; is count incorrect or file otherwise damaged?")
                parts = utils.to_unicode(line.rstrip(), encoding=encoding, errors=unicode_errors).split(" ")
                if len(parts) != vector_size + 1:
                    raise ValueError("invalid vector on line %s (is this really the text format?)" % line_no)
                word, weights = parts[0], [REAL(x) for x in parts[1:]]
                add_word(word, weights)
    if result.syn0.shape[0] != len(result.vocab):
        logger.info(
            "duplicate words detected, shrinking matrix size from %i to %i",
            result.syn0.shape[0], len(result.vocab)
        )
        result.syn0 = ascontiguousarray(result.syn0[: len(result.vocab)])
    assert (len(result.vocab), vector_size) == result.syn0.shape

    logger.info("loaded %s matrix from %s", result.syn0.shape, fname)
    return result
