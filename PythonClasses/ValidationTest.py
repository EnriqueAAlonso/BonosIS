import unittest
from ValidateInputs import ValidateInputs

class ValidationTest(unittest.TestCase):
    def test_flavor(self):
        validation=ValidateInputs()
        resultado=validation.validateFlavor("TestString")
        self.assertNotEqual(resultado,False, "El resultado no debio ser falso")
        self.assertEqual(resultado, False, "El resultado es incorrecto")
    def test_Bono(self):
        validation=ValidateInputs()
        resultado=validation.validateBono("TestString")
        self.assertEqual(resultado,False, "El resultado no debio ser verdadero")
        resultado=validation.validateBono("123123123")
        self.assertEqual(resultado, False, "El resultado es incorrecto")
    def test_Usuario(self):
        validation=ValidateInputs()
        resultado=validation.validateBono("TestString")
        self.assertEqual(resultado,False, "El resultado no debio ser verdadero")
        resultado=validation.validateBono("123123123")
        self.assertEqual(resultado, False, "El resultado es incorrecto")
    