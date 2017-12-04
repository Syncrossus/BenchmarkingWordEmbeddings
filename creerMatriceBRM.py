import xlrd
from xlwt import Workbook, Formula
import numpy as np

matriceBRM = np.zeros((541,541))

classeur = xlrd.open_workbook('cos_matrix_brm_IFR.xlsx')

nom_des_feuilles = classeur.sheet_names()
numeroColonne = [0,200,400]
for i in range(3):
	sh = classeur.sheet_by_name(nom_des_feuilles[i])
	for colnum in range(1,sh.ncols):
		for element in range(1,542):
			matriceBRM[colnum - 1+numeroColonne[i]][element-1] = sh.col(colnum)[element].value

