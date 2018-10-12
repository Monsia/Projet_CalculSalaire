

import unittest
from Calcul_Salaire import *


class MyFirstTests(unittest.TestCase):

    def test_calcul_salaire1(self):
        self.assertEqual(CalculSalaire("Architecte", 4), "4000")

    def test_calcul_salaire2(self):
        self.assertEqual(CalculSalaire("Médecin", 8), "7000")

    def test_calcul_salaire3(self):
        self.assertEqual(CalculSalaire("Consultant", 5), "5000")