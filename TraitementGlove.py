import gensim
from gensim.models.keyedvectors import KeyedVectors

#Convertir le modèle Glove en Word2vec
gensim.scripts.glove2word2vec.glove2word2vec('Chemin\\glove.840B.300d.txt', 'chemin\\gloveTruque300.txt')

#Charger le nouveau fichiern qui constitue un modèle
word_vectors = KeyedVectors.load_word2vec_format('Chemin\\gloveTruque300.txt')