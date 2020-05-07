import logging
import traceback
logging.basicConfig(level=logging.DEBUG, filename='events.log')
#logging.basicConfig(level=logging.DEBUG, filename="validationEvents.log")

class ValidateInputs:
    def validateIdBono(self,IdBono ):
        '''
        Funcion valida el tipo de dato del bono
        
        Parameters
        ----------
        IdBono : str
            Identificador del bono.

        Returns
        -------
        bool
            Resultado si el tipo de dato es correcto o incorrecto.

        '''
        logging.info("Entra a la funcion de validacion de bono con el bono {}".format(IdBono))
        try:
            int(IdBono)
            logging.debug("Se valido que la variable {} fuera convertida correctamente a un int".format(IdBono))
            return True
        except ValueError:
            logging.error("Ocurrio un problema al convertir {} en un entero".format(IdBono))
            return False
    def validateIdUsuario(self, IdUsuario):
        '''
        Funcion para verificar si la IdUsuario es valida

        Parameters
        ----------
        IdUsuario : string
            Identificador del usuario creador del bono.

        Returns
        -------
        bool
            validacion si es un tipo de dato valido.

        '''
        logging.info("Entra a la funcion de la validacio del identificador del usuaario con el ID de Usuario {}".format(IdUsuario))
        try:
            int(IdUsuario)
            logging.debug("Se valido que la variable {} fuera convertida correctamente a un int".format(IdUsuario))
            return True
        except ValueError:
            logging.error("Ocurrio un problema al convertir {} en un entero".format(IdUsuario))
            return False
    def validateFlavor(self, flavor):
        '''
        funcion para validar el flavor del bono

        Parameters
        ----------
        flavor : string
            string que da el flavor del bono.

        Returns
        -------
        bool
            Resultado de la validacion del tipo de dato.

        '''
        logging.info("Se recibio el siguiente flavor {}".format(flavor))
        return isinstance(flavor, str)
        
