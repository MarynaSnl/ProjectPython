import unittest
import math
import Proj_2


class my_test(unittest.TestCase):
    def setUp(self):
        self.inzynier = Proj_2.Inzynier("Jan") 
        self.naukowec = Proj_2.Naukowec("Olek")

    def test_oblicz_stezenie_molowe_roztworu(self):
        self.assertEqual(self.naukowec.oblicz_stezenie_molowe_roztworu(25, 5), 5)
        self.assertEqual(self.naukowec.oblicz_stezenie_molowe_roztworu(100, 33), 3.0303)
        self.assertFalse(self.naukowec.oblicz_stezenie_molowe_roztworu(10, 0))
        
    def test_oblicz_procent_liczbu(self):
        self.assertEqual(self.naukowec.oblicz_procent_liczbu(100, 12, 1), 12)
        self.assertEqual(self.naukowec.oblicz_procent_liczbu(100, 7, 2), 7)
        self.assertFalse(self.naukowec.oblicz_procent_liczbu(0, 7, 2))


    def test_wypisz_ciag_fibbonacciego(self):
        self.assertEqual(self.inzynier.wypisz_ciag_fibbonacciego(00), [0])
        self.assertEqual(self.inzynier.wypisz_ciag_fibbonacciego(1), [0,1])
        self.assertEqual(self.inzynier.wypisz_ciag_fibbonacciego(7), [0,1,1,2,3,5,8,13])

    def test_oblicz_pole_i_obwod_okregu(self):
        self.assertEqual(self.inzynier.oblicz_pole_i_obwod_okregu(3, False), "Promien:3,wynik-Pole:"+str(round(2*math.pi*3,5))+",Obwod:" + str(round(math.pi*3*3,5)))


#if __name__ == '__main__':
#    unittest.main()