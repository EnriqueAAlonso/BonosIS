import math
import logging
import traceback
logging.basicConfig(level=logging.DEBUG, filename='events.log')
class ISIN:

    def validateISIN(self,ISIN):
        '''
        Funcion que valida el ISIN obtenido

        Parameters
        ----------
        ISIN : str
            Identificador del bono.

        Returns
        -------
        bool
            Resultado si el ISIN concuerda

        '''
        logging.info("\n Entra a la funcion de validacion de ISIN con ISIN {}".format(ISIN))
        prefix=ISIN[0:2]
        cusip=ISIN[2:-1]
        result=int(ISIN[-1])
        numericalPrefix = ""
        if (prefix == 'US'):

            numericalPrefix = '3028'
        else:
            numericalPrefix = '0000'
        compare=createCheckSum(numericalPrefix,cusip)
        if(compare!=result):
            logging.info("checkSum original {} no es igual al valor {}".format(compare, result))
            return False
        logging.info("checkSum creado es valido, con valor  {}".format( result))
        return True

    def createCheckSum(self,numericalPrefix, cusip):
            """

            :param numericalPrefix: prefijo de 2 letras correspondientes al inicio del ISIN
            :param cusip: arreglo de numeros
            :return: valor resultante de las operaciones necesarias para crear el ISIN
            """


            logging.info("\n El prefijo obtenido del ISIN tiene un valor de  {}".format(numericalPrefix))
            evenArr = []
            oddArr = []
            for i in range(0, 4):
                if (i % 2 == 0):
                    oddArr.append(int(numericalPrefix[i]))

                else:
                    evenArr.append(int(numericalPrefix[i]))
            for i in range(len(cusip)):
                if (i % 2 == 0):
                    oddArr.append(int(cusip[i]))

                else:
                    evenArr.append(int(cusip[i]))
            logging.info("El arreglo impar es   {}".format(oddArr))
            logging.info("El arreglo par es   {}".format(evenArr))

            for i in range(len(oddArr)):
                oddArr[i]=oddArr[i]*2
            logging.info("El arreglo impar despues de la multiplicacion es {}".format(oddArr))
            sum = 0
            for i in range(len(evenArr)):
                sum += evenArr[i]
                logging.info("Se ha sumado {},de los pares el valor final de la suma es {}".format(str(evenArr[i]), str(sum)))
            for i in range(len(oddArr)):
                if (len(str(oddArr[i])) > 1):
                    logging.info("Se separo el siguiente {} en dos digitos".format(str(oddArr[i])))
                    digit=str(oddArr[i])[0]
                    sum += int(digit)
                    logging.info("Se ha sumado {}, de los impares el valor final de la suma es {}", format(digit, str(sum)))
                    digit = str(oddArr[i])[1]
                    sum += int(digit)
                    logging.info("Se ha sumado {}, el valor final de la suma es {}".format(digit, str(sum)))
                else:
                    sum += oddArr[i]
                    logging.info("Se ha sumado {}, el valor final de la suma es {}".format(str(oddArr[i]), str(sum)))
            sum = sum % 10
            sum = 10 - sum
            sum - sum % 10
            logging.info("checkSum creado con valor {}".format(sum))
            return sum

    def CreateISINFromCusip(self,prefix,cusip):
        """

        :param prefix: prefijo usado para la creacion del ISIN que denota el pais de origen
        :param cusip: arreglo numerico usado para el calculo del ISIN
        :return: Se regresa el ISIN ya creado
        """
        logging.info("\n Entra a la funcion de creacion de ISIN con Cusip {} y prefijo {}".format(cusip,prefix))


        numericalPrefix = ""
        if (prefix == 'US'):

            numericalPrefix = '3028'
        else:
            numericalPrefix = '0000'
        if (prefix == 'US'):

            numericalPrefix = '3028'
        else:
            numericalPrefix = '0000'
        cSum=createCheckSum(numericalPrefix, cusip)
        logging.info("Checksum creado con valor {} ".format(str(cSum)))
        logging.info("ISIN final con valor {}".format(prefix+cusip+str(cSum)))
        return prefix+cusip+str(cSum)

isin=ISIN()
print(createCheckSum("3028","037833100"))



