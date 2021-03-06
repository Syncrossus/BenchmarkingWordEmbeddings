import xlrd
import numpy as np
from constants import *


def importMatrixBRM():
    matriceBRM = np.zeros((541, 541))

    classeur = xlrd.open_workbook(RAW_CSV_DIR + COS_BRM_XLS)

    nom_des_feuilles = classeur.sheet_names()
    numeroColonne = [0, 200, 400]
    for i in range(3):
        sh = classeur.sheet_by_name(nom_des_feuilles[i])
        for colnum in range(1, sh.ncols):
            for element in range(1, 542):
                matriceBRM[colnum - 1 + numeroColonne[i]][element - 1] = sh.col(colnum)[element].value

    # Pour obtenir les indexs des termes de la matrice BRM
    listeTerme = []
    sh = classeur.sheet_by_name(nom_des_feuilles[0])
    for i in range(1, 542):
        listeTerme.append(sh.col(0)[i].value)
    return (matriceBRM, listeTerme)


if __name__ == '__main__':
    matriceBRM = importMatrixBRM()
    # Exemple d'utilisation pour piocher la case entre ambulance et airplane de la matriceBRM
    print(matriceBRM[listeTerme.index('ambulance')][listeTerme.index('airplane')])
