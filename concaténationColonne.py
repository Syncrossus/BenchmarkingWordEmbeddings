import csv

fichier = open('wordsim.csv', "rt")
read = csv.reader(fichier,delimiter=";")

#Concaténation de trois colonnes en un tuple de mots et un score
a = np.matrix([[(i[0], i[1]), float(i[2])] for i in read])