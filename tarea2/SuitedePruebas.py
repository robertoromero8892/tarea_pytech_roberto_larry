'''Suite de casos de pruebas
Autores:
Roberto Romero10-10642
Larry Perez 10-10547
'''
import unittest
from datetime import datetime
from tarea2 import Tarifa, calcularPrecio 

class Test(unittest.TestCase):
    
        def testprueba(self):
            tari = Tarifa (1,1)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=3)]
            resultado = calcularPrecio(tari,tiempo)
            assert resultado == 48.00    
 
if __name__ == "__main__":
    unittest.main()      