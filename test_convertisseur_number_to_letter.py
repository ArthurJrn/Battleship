from IA_aux import *
import numpy as np
plateau = np.zeros((10, 10))

def test_convertisseur_number_to_letter():
	assert(convertir_tir_number_to_letter(7,2) == "B8"), "Erreur : la conversion aurait du donner B8"
	assert(convertir_tir_number_to_letter(0,0) == "A1"), "Erreur : la conversion aurait du donner A1"
	assert(convertir_tir_number_to_letter(0,2) == "B1"), "Erreur : la conversion aurait du donner B1"
	assert(convertir_tir_number_to_letter(3,3) == "C4"), "Erreur : la conversion aurait du donner C4"
	assert(convertir_tir_number_to_letter(4, 4) == "D5"), "Erreur : la conversion aurait du donner D5"
	assert(convertir_tir_number_to_letter(9, 10) == "J10"), "Erreur : la conversion aurait du donner J10"
	assert(convertir_tir_number_to_letter(2,2) == "B3"), "Erreur : la conversion aurait du donner B3"
	assert(convertir_tir_number_to_letter(2,7) == "G3"), "Erreur : la conversion aurait du donner G3"
	print("All tests are successful !")


if __name__ == '__main__':
	test_convertisseur_number_to_letter()
	
