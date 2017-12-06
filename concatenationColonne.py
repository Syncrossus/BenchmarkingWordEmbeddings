import csv
import numpy as np
from constants import *
from lireObjet import read

matrices = []

with open(WORDSIM, 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=';')
    # Concaténation de trois colonnes en un tuple de mots et un score
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader]))

with open(MC_CSV, 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=";")
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader if any(i)]))

with open(MTURK, 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=',')
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader]))

with open(REL122, 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=',')
    matrices.append(np.matrix([[(i[1], i[2]), float(i[0])] for i in reader]))

with open(RG, 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=';')
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader if any(i)]))

with open(SIMLEX, 'rt')as fichier:
    reader = csv.reader(fichier, delimiter='\t')
    next(reader)
    matrices.append(np.matrix([[(i[0], i[1]), float(i[3])] for i in reader]))

with open(UMNSRS_REL, 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=',')
    matrices.append(np.matrix([[(i[2], i[3]), float(i[0])] for i in reader]))

with open(UMNSRS_SIM, 'rt')as fichier:
    reader = csv.reader(fichier, delimiter=',')
    matrices.append(np.matrix([[(i[2], i[3]), float(i[0])] for i in reader]))

data = read('matriceCosBrm')
listeTerme = read('listetermeBRM')
matrices.append([[(listeTerme[i], listeTerme[j]), float(data[i][j])] for j in range(0, 541) for i in range(j + 1, 541) if data[i][j] != 0.0])
