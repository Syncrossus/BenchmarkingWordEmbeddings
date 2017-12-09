import csv
import numpy as np
from constants import *
from lireObjet import read

files = [WORDSIM, MC_CSV, MTURK, REL122, RG, SIMLEX, UMNSRS_REL, UMNSRS_SIM]
delim = [';', ';', ',', ',', ';', '\t', ',', ',']
order = [(0, 1, 2), (0, 1, 2), (0, 1, 2), (1, 2, 0), (0, 1, 2), (0, 1, 3), (2, 3, 0), (2, 3, 0)]
contains_header = [False, False, False, False, False, True, True, True]


for i in range(len(files)):
    with open(RAW_CSV_DIR + files[i], 'rt') as readfile:
        reader = csv.reader(readfile, delimiter=delim[i])
        with open(NEW_CSV_DIR + files[i], 'w', newline='') as writefile:
            writer = csv.writer(writefile)
            if(contains_header[i]):
                next(reader)
            # Concaténation de trois colonnes en un tuple de mots et un score
            writer.writerows([[row[order[i][0]], row[order[i][1]], float(row[order[i][2]])] for row in reader if any(row)])

"""
with open(RAW_CSV_DIR + WORDSIM, 'rt') as readfile:
    reader = csv.reader(readfile, delimiter=';')
    # Concaténation de trois colonnes en un tuple de mots et un score
    with open(NEW_CSV_DIR + WORDSIM, 'w', newline='') as writefile:
        writer = csv.writer(writefile)
        writer.writerows([[(i[0], i[1]), float(i[2])] for i in reader])

with open(RAW_CSV_DIR + MC_CSV, 'rt') as readfile:
    reader = csv.reader(readfile, delimiter=";")
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader if any(i)]))

with open(RAW_CSV_DIR + MTURK, 'rt') as readfile:
    reader = csv.reader(readfile, delimiter=',')
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader]))

with open(RAW_CSV_DIR + REL122, 'rt') as readfile:
    reader = csv.reader(readfile, delimiter=',')
    matrices.append(np.matrix([[(i[1], i[2]), float(i[0])] for i in reader]))

with open(RAW_CSV_DIR + RG, 'rt') as readfile:
    reader = csv.reader(readfile, delimiter=';')
    matrices.append(np.matrix([[(i[0], i[1]), float(i[2])] for i in reader if any(i)]))

with open(RAW_CSV_DIR + SIMLEX, 'rt') as readfile:
    reader = csv.reader(readfile, delimiter='\t')
    next(reader)
    matrices.append(np.matrix([[(i[0], i[1]), float(i[3])] for i in reader]))

with open(RAW_CSV_DIR + UMNSRS_REL, 'rt') as readfile:
    reader = csv.reader(readfile, delimiter=',')
    matrices.append(np.matrix([[(i[2], i[3]), float(i[0])] for i in reader]))

with open(RAW_CSV_DIR + UMNSRS_SIM, 'rt') as readfile:
    reader = csv.reader(readfile, delimiter=',')
    matrices.append(np.matrix([[(i[2], i[3]), float(i[0])] for i in reader]))

data = read('matriceCosBrm')
listeTerme = read('listetermeBRM')
matrices.append([[(listeTerme[i], listeTerme[j]), float(data[i][j])] for j in range(0, 541) for i in range(j + 1, 541) if data[i][j] != 0.0])
"""
