import csv
from constants import *
from lireObjet import read

files = [WORDSIM, MC_CSV, MTURK, REL122, RG, SIMLEX, UMNSRS_REL, UMNSRS_SIM]  # filenames for CSVs
delim = [';', ';', ',', ',', ';', '\t', ',', ',']  # delimiters for each file
order = [(0, 1, 2), (0, 1, 2), (0, 1, 2), (1, 2, 0), (0, 1, 2), (0, 1, 3), (2, 3, 0), (2, 3, 0)]  # column indices of word1, word2 and similarity score in each file
contains_header = [False, False, False, False, False, True, True, True]  # some files contain a first row with column headers, which we need to get rid of


for i in range(len(files)):
    with open(RAW_CSV_DIR + files[i], 'rt') as readfile:
        reader = csv.reader(readfile, delimiter=delim[i])
        with open(NEW_CSV_DIR + files[i], 'w', newline='') as writefile:
            writer = csv.writer(writefile)
            if(contains_header[i]):  # If the first row contains column names
                next(reader)  # popping the first row off of the iterator
            # extracting word1, word2, and similarity score for each row of each CSV and writing it to a file in that order
            writer.writerows([[row[order[i][0]], row[order[i][1]], float(row[order[i][2]])] for row in reader if any(row)])
            # for row in reader if any(row) : each row in the CSV file that is not empty
            # [row[order[i][0]], row[order[i][1]], float(row[order[i][2]])] : list containing 3 fields : word1, word2, similarityScore.
            # Each tuple in `order` contains the indices of each field in a row of the CSV.

data = read('matriceCosBrm')
listeTerme = read('listetermeBRM')
matrices.append([[(listeTerme[i], listeTerme[j]), float(data[i][j])] for j in range(0, 541) for i in range(j + 1, 541) if data[i][j] != 0.0])
