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
            #Test de tarifa cero
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
            #Test con ocho dias
            tari = Tarifa (1,1)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=8,second=1)]
            self.assertRaises(Exception,calcularPrecio,tari,tiempo) 
            
        def testTiempoMaxFront(self):
            #Test de frontera maximo de tiempo (7 dias, 1 seg)
            tari = Tarifa (1,1)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=8,second=1)]
            self.assertRaises(Exception,calcularPrecio,tari,tiempo) 
            
        def testTiempoMinFront(self):
            #Test de frontera minimo de tiempo (14 mins 59 segs)
            tari = Tarifa (1,1)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=8,minute=14,second=59)]
            self.assertRaises(Exception,calcularPrecio,tari,tiempo)
            
        def testTarifasFrontInferior(self):
            #Test de viernes a las 23:59:59 a domingo a las 23:59:59 con diferentes tarifas
            tari = Tarifa (1,2)
            tiempo = [datetime(year=2015,month=1,day=2,hour=23,minute=59,second=59),datetime(year=2015,month=1,day=4,hour=23,minute=59,second=59)]
            calcularPrecio(tari,tiempo)
            
        
        def testTarifasFrontSuperior(self):
            #Test de sabado a las 00:00:01 a lunes a las 00:00:01 con diferentes tarifas
            tari = Tarifa (1,2)
            tiempo = [datetime(year=2015,month=1,day=3,second=1),datetime(year=2015,month=1,day=5,second=1)]
            calcularPrecio(tari,tiempo)
            
        
        #tests maliciosos
        
        def testLetras(self): 
            self.assertRaises(Exception,calcularPrecio,'a','b') 
            
        def testTarifaNoEntera(self):
            tari = Tarifa (1.5,1.5)
            tiempo = [datetime(year=2015,month=1,day=1,hour=1),datetime(year=2015,month=1,day=1,hour=2)] 
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
            
        def testTiempoCero(self):
            #Test de tiempo cero
            tari = Tarifa (1,1)
            tiempo = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=1)]
            self.assertRaises(Exception,calcularPrecio,tari,tiempo)
            
        def testTiempoNeg(self):
            #Test de tiempo negativo
            tari = Tarifa (1,1)
            tiempo = [datetime(year=2015,month=1,day=2),datetime(year=2015,month=1,day=1)]
            self.assertRaises(Exception,calcularPrecio,tari,tiempo)  
            
        def testTarifasEsquina(self):
            #Test de viernes a las 23:59:59 a lunes a las 00:00:01 con diferentes tarifas
            tari = Tarifa (1,2)
            tiempo = [datetime(year=2015,month=1,day=2,hour=23,minute=59,second=59),datetime(year=2015,month=1,day=5,second=1)]
            resultado = calcularPrecio(tari, tiempo)
            assert resultado == 96.00
        
        def testTarifasEsquina2(self):
            #Test de viernes a las 23:00:00 a lunes a las 01:00:00 con diferentes tarifas
            tari = Tarifa (1,2)
            tiempo = [datetime(year=2015,month=1,day=2,hour=23),datetime(year=2015,month=1,day=5,hour=1)]
            resultado = calcularPrecio(tari, tiempo)
            assert resultado == 98.00
                
        def testTarifasRedondeo(self):
            
            #prueba de redondeo a centimos
            
            tari1 = Tarifa (1,1)
            tiempo1 = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=2)]
            price1 = calcularPrecio(tari1,tiempo1)
            
            
            tari2 = Tarifa (1.000001,1.000001)
            tiempo2 = [datetime(year=2015,month=1,day=1),datetime(year=2015,month=1,day=2)]
            price2 = calcularPrecio(tari2,tiempo2)

        
            assert price1==price2
        
if __name__ == "__main__":
    unittest.main()      
