import csv
import numpy as np
from constants import *

matrices = []
CSVLIST = [WORDSIM, MC_CSV, MTURK, REL122, RG]

with open(WORDSIM[0], 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=WORDSIM[1])
    # Concaténation de trois colonnes en un tuple de mots et un score
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader]))

with open(MC_CSV[0], 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=MC_CSV[1])
    # Concaténation de trois colonnes en un tuple de mots et un score
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader if any(i)]))

with open(MTURK[0], 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=MTURK[1])
    # Concaténation de trois colonnes en un tuple de mots et un score
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader]))

with open(REL122[0], 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=REL122[1])
    # Concaténation de trois colonnes en un tuple de mots et un score
    matrices.append(np.matrix([[(i[1], i[2]), float(i[0])] for i in reader]))

with open(RG[0], 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=RG[1])
    # Concaténation de trois colonnes en un tuple de mots et un score
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader if any(i)]))
