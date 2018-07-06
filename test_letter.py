from IA_aux import *
import numpy as np
plateau= np.zeros((10,10))

def test_letter_to_number () :
    assert(convertir_tir_letter_to_number("C5") == (4,2)), "Erreur : la conversion de C5 devrait donner (4,2)"
    assert(convertir_tir_letter_to_number("D10") == (9,3)), "Erreur : la conversion de D10 devrait donner (9,3)"
    assert(convertir_tir_letter_to_number("E7") == (6,4)), "Erreur : la conversion de E7 devrait donner (6,4)"
    assert(convertir_tir_letter_to_number("A1") == (0,0)), "Erreur : la conversion de A1 devrait donner (0,0)"
    assert(convertir_tir_letter_to_number("J10") == (9,9)), "Erreur : la conversion de J10 devrait donner (9,9)"
    assert(convertir_tir_letter_to_number("G3") == (2,6)), "Erreur : la conversion de G3 devrait donner (2,6)"

if __name__=='__main__' :
 
    test_letter_to_number()
