import unittest
from ISBNCreation import ISIN

class IsinTest(unittest.TestCase):
    def test_create(self):
        isin=ISIN()
        resultado=isin.createCheckSum("3028","037833100")
        self.assertEqual(resultado, 5, "El resultado es incorrecto")
    def test_validate(self):
        isin=ISIN()
        resultado=isin.validateISIN("US0378331005")
        self.assertNotEqual(resultado, False, "El resultado no debio ser falso")
        self.assertEqual(resultado, True, "El resultado es incorrecto")

    def test_createCusip(self):
        isin = ISIN()
        resultado = isin.CreateISINFromCusip("3028","037833100")
        self.assertEqual(resultado, "US0378331005", "El resultado es incorrecto")

unittest.main()