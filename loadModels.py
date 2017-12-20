from gensim.models.keyedvectors import KeyedVectors
from constants import *

# Load Google's pre-trained Word2Vec model.


def load_google_news():
    return KeyedVectors.load_word2vec_format(GOOGLE_NEWS, binary=True)


def load_glove():
    import gensim
    # Convertir le modele Glove en Word2vec
    gensim.scripts.glove2word2vec.glove2word2vec(GLOVE, 'glove_as_w2v.txt')
    # Charger le nouveau fichier qui constitue un modele
    return KeyedVectors.load_word2vec_format('glove_as_w2v.txt')


def load_text8():
    sentences = word2vec.Text8Corpus(TEXT8)
    return word2vec.Word2Vec(sentences, size=300, window=12, min_count=25, workers=3, sg=1, negative=12)


def load(modelname):
    if modelname == GOOGLE_NEWS:
        return load_google_news()
    elif modelname == TEXT8:
        return load_text8()
    else:
        return load_glove()
