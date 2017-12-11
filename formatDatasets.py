import csv
import numpy as np

from constants import *
from lireObjet import read


def is_synonymy_file(filename):
    if filename in [MC_CSV, RG, SIMLEX]:
        return True
    return False


files = [WORDSIM, MC_CSV, MTURK, REL122, RG, SIMLEX]  # filenames for CSVs
delim = [';', ';', ',', ',', ';', '\t']  # delimiters for each file
order = [(0, 1, 2), (0, 1, 2), (0, 1, 2), (1, 2, 0), (0, 1, 2), (0, 1, 3)]  # column indices of word1, word2 and similarity score in each file
scale = [(0, 10), (0, 4), (1, 5), (0, 4), (0, 4), (0, 10)]  # min and max values on the grading scale for eachfile, found from various websites with metadata on the datasets
contains_header = [False, False, False, False, False, True]  # some files contain a first row with column headers, which we need to get rid of

synonymy_pairs = []
relatedness_pairs = []

for i in range(len(files)):
    with open(RAW_CSV_DIR + files[i], 'rt') as readfile:
        reader = csv.reader(readfile, delimiter=delim[i])
        if(contains_header[i]):  # If the first row contains column names
            next(reader)  # popping the first row off of the iterator
        # extracting word1, word2, and similarity score for each row of each CSV and writing it to a list in that order
        file_formatted = [[row[order[i][0]], row[order[i][1]], float(row[order[i][2]])] for row in reader if any(row)]
        # for row in reader if any(row) : each row in the CSV file that is not empty
        # [row[order[i][0]], row[order[i][1]], float(row[order[i][2]])] : list containing 3 fields : word1, word2, similarityScore.
        # Each tuple in `order` contains the indices of each field in a row of the CSV.
        scores = np.array([row[2] for row in file_formatted])  # isolating scores for normalization
        scores = (scores - scale[i][0]) / (scale[i][1] - scale[i][0])  # normalization
        file_formatted = [[file_formatted[i][0], file_formatted[i][1], scores[i]] for i in range(len(file_formatted))]  # re-writing normalized scores
        if is_synonymy_file(files[i]):
            synonymy_pairs += file_formatted
        else:
            relatedness_pairs += file_formatted

# writing synonymy pairs to file
with open(NEW_CSV_DIR + "synonymy.csv", 'w', newline='') as writefile:
    writer = csv.writer(writefile)
    writer.writerows(synonymy_pairs)

# writing relatedness pairs to file
with open(NEW_CSV_DIR + "relatedness.csv", 'w', newline='') as writefile:
    writer = csv.writer(writefile)
    writer.writerows(relatedness_pairs)

"""
, UMNSRS_REL, UMNSRS_SIM
, ',', ','
, (2, 3, 0), (2, 3, 0)
, (), ()
, True, True
"""


matriceCosBrm = read('matriceCosBrm')
listeTermeBRM = read('listetermeBRM')
cos_brm_pairs = [[listeTermeBRM[i], listeTermeBRM[j], float(matriceCosBrm[i][j])] for j in range(0, 541) for i in range(j + 1, 541) if matriceCosBrm[i][j] != 0.0]
with open(NEW_CSV_DIR + COS_BRM_CSV, 'w', newline='') as writefile:
    writer = csv.writer(writefile)
    writer.writerows(cos_brm_pairs)
