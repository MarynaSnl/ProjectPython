import unittest
from Proj_2 import *
#import math 

class my_test(unittest.TestCase):
   
    def oblicz_BMI(self):
        self.assertEqual(dodaj(3,6,12), 21)
    #def test_wpisz_imie(self):
    #    self.assertEqual(wpisz_imie(imie = "Jan Nowak"), "Dzien dobry, Jan Nowak")
    #def test_pole_kola(self):
    #    self.assertEqual(pole_kola(3), 6* math.pi)