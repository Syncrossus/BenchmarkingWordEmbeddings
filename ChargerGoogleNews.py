import gensim
# Load Google's pre-trained Word2Vec model.
model = KeyedVectors.load_word2vec_format('Chemin\\GoogleNews-vectors-negative300.bin', binary=True)