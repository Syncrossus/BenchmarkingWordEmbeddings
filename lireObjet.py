import pickle

def read(file):
    with open(file, 'rb') as fichier:
        mon_depickler = pickle.Unpickler(fichier)
        d_recupere = mon_depickler.load()
        return d_recupere


data = read("modeltext8")