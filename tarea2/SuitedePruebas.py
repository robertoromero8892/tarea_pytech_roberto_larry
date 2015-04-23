'''Suite de casos de pruebas para la funcion CalcularPrecio() 
Creado el 19/04/2015
Equipo:Pytech
Autores:
Roberto Romero10-10642
Larry Perez 10-10547
'''

import unittest
from datetime import datetime
from tarea2 import Tarifa, calcularPrecio 

class Test(unittest.TestCase):
    
        def testTarifaCero(self):
            tari = Tarifa (0,0)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=3)]
            resultado = calcularPrecio(tari,tiempo)
            assert resultado == 0.00    
        
        def testTarifaMax(self):
            tari = Tarifa (257698037700,257698037700)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=8)]
            calcularPrecio(tari,tiempo)
        
        def test7Dias(self):
            tari = Tarifa (1,1)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=8)]
            resultado = calcularPrecio(tari,tiempo)
            assert resultado == 168.00 
                
        def testMaxDias(self):
            tari = Tarifa (1,1)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=8,second=1)]
            self.assertRaises(Exception,calcularPrecio,tari,tiempo) 

        def testMinTiempo(self):
            tari = Tarifa (1,1)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=1,minute=14,second=59)]
            self.assertRaises(Exception,calcularPrecio,tari,tiempo) 
        
        #tests maliciosos
        
        def testLetras(self):
            tari = Tarifa ('a','b')
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=8)]
            calcularPrecio(tari,tiempo) 
            
        def testTarifaNoEntera(self):
            tari = Tarifa (1.5,1.5)
            tiempo = [datetime(year=2015,month=1,day=1,hour=1),datetime(year=2015,month=1,day=1,hour=2)]
            print(calcularPrecio(tari,tiempo))  
            resultado = calcularPrecio(tari,tiempo)
            assert resultado == 1.50

        def testFraccionesHora(self):
            tari = Tarifa (1,2)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=1,hour=1,minute=1)]
            resultado = calcularPrecio(tari,tiempo)
            assert resultado == 2.00
            
        def testNegativos(self):
            tari = Tarifa (-1,-1)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=3)]
            self.assertRaises(Exception,calcularPrecio,tari,tiempo)
            
        
if __name__ == "__main__":
    unittest.main()      