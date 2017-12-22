from gensim.models.keyedvectors import KeyedVectors
from constants import *
from gensim.models import word2vec


def load_google_news(enable_print=True):
    if enable_print:
        print("Loading Google News pretrained model...")
    # Load Google's pre-trained Word2Vec model.
    return KeyedVectors.load_word2vec_format(GOOGLE_NEWS, binary=True)


def load_glove(enable_print=True):
    if enable_print:
        print("Loading GloVe model...")
    import gensim
    # Convertir le modele Glove en Word2vec
    gensim.scripts.glove2word2vec.glove2word2vec(GLOVE, 'glove_as_w2v.txt')
    # Charger le nouveau fichier qui constitue un modele
    return KeyedVectors.load_word2vec_format('glove_as_w2v.txt')


def load_text8(enable_print=True):
    if enable_print:
        print("Training Text8 model...")
    sentences = word2vec.Text8Corpus(TEXT8)
    return word2vec.Word2Vec(sentences, size=300, window=12, min_count=25, workers=3, sg=1, negative=12)


def load(modelname, enable_print=True):
    if modelname == GOOGLE_NEWS:
        return load_google_news(enable_print)
    elif modelname == TEXT8:
        return load_text8(enable_print)
    else:
        return load_glove(enable_print)
