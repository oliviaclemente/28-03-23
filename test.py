import unittest
from persona import Persona, EstadoHospitalario


class TestPersona(unittest.TestCase):
    def setUp(self):
        self.persona1 = Persona("11111111A", "Juan", EstadoHospitalario.UCI, 45, 100, 0, 3)
        self.persona2 = Persona("22222222B", "María", EstadoHospitalario.PLANTA, 30, 100, 1, 3)
    
    def test_constructor(self):
        with self.assertRaises(ValueError):
            Persona("11111111A", "Pedro", EstadoHospitalario.UCI, 25, 100, 0, 3)
        
        with self.assertRaises(ValueError):
            Persona("33333333C", "Pepe", "crítico", 60, 100, 2, 3)
        
        with self.assertRaises(ValueError):
            Persona("44444444D", "Lucía", EstadoHospitalario.UCI, 110, 100, 0, 3)
        
        with self.assertRaises(ValueError):
            Persona("55555555E", "Ana", EstadoHospitalario.PLANTA, 20, 100, 3, 3)
        
        with self.assertRaises(ValueError):
            Persona("66666666F", "Carlos", EstadoHospitalario.PLANTA, 50, 2, 0, 3)
        
        with self.assertRaises(ValueError):
            Persona("77777777G", "Sofía", EstadoHospitalario.PLANTA, 70, 100, 4, 3)
        
        with self.assertRaises(ValueError):
            Persona("88888888H", "José", EstadoHospitalario.PLANTA, 40, 100, 0, 5)
        
        with self.assertRaises(ValueError):
            Persona("99999999I", "Miguel", EstadoHospitalario.PLANTA, 18, 100, 0, 3)
    
    def test_get_CargaViral(self):
        self.assertEqual(self.persona1.get_CargaViral(), 55)
        self.assertEqual(self.persona2.get_CargaViral(), 70)
    
    def test_get_dni(self):
        self.assertEqual(self.persona1.get_dni(), "11111111A")
        self.assertEqual(self.persona2.get_dni(), "22222222B")
    
    def test_get_max_edad(self):
        self.assertEqual(self.persona1.get_max_edad(), 100)
        self.assertEqual(self.persona2.get_max_edad(), 100)
    
    def test_get_list_dnis(self):
        lista_dnis = Persona.get_list_dnis()
        self.assertEqual(len(lista_dnis), 2)
        self.assertIn("11111111A", lista_dnis)
        self.assertIn("22222222B", lista_dnis)
    
    def test_get_max_dosis(self):
        self.assertEqual(self.persona1.get_max_dosis(), 3)
        self.assertEqual(self.persona2.get_max_dosis(), 3)
    
    def test_set_CargaViral(self):
        self.persona1.set_CargaViral(50)
        self.assertEqual(self.persona1.get_CargaViral(), 50)
    
    def test_eliminarUsuario(self):
        Persona.eliminarUsuario(self.persona1.get_dni())
        lista_dnis = Persona.get_list_dnis()
        self.assertEqual(len(lista_dnis), 1)
        self.assertNotIn("11111111A", lista_dnis)
    
    def test_str(self):
        persona_str = str(self.persona1)
        self.assertIn("
