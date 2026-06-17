# test_sistema.py
import unittest
from sistema import CarteraInversion, ProyectoMinero

class TestCarteraMinera(unittest.TestCase):
    
    def test_suma_proyectos_nuevos_debe_ser_3794(self):
        # 1. Arrange (Preparar los datos de la lectura)
        cartera = CarteraInversion()
        
        cartera.agregar_proyecto(ProyectoMinero("Reposición Ferrobamba", 1753, "Nuevo"))
        cartera.agregar_proyecto(ProyectoMinero("Coimolache Sulfuros", 598, "Nuevo"))
        cartera.agregar_proyecto(ProyectoMinero("Mina Justa Subterránea", 500, "Nuevo"))
        cartera.agregar_proyecto(ProyectoMinero("Reposición Colquijirca", 431, "Nuevo"))
        cartera.agregar_proyecto(ProyectoMinero("Ampliación Huancapetí", 345, "Nuevo"))
        cartera.agregar_proyecto(ProyectoMinero("Ampliación Huachocolpa", 167, "Nuevo"))

        # 2. Act (Ejecutar la función que queremos probar)
        resultado_calculado = cartera.calcular_total_por_tipo("Nuevo")

        # 3. Assert (Verificar si el resultado es igual al esperado de US$ 3794M)
        self.assertEqual(resultado_calculado, 3794)

if __name__ == '__main__':
    unittest.main()