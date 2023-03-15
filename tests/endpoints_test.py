import unittest
from fastapi.testclient import TestClient
from main import app

class TestInvertNumber(unittest.TestCase):
    
    def setUp(self):
        self.client = TestClient(app)
    
    def test_inverter_digitos_positivos(self):
        response = self.client.get("/reverse-int/12345")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"numero invertido": 54321})
    
    def test_inverter_digitos_negativos(self):
        response = self.client.get("/reverse-int/-12345")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"numero invertido": -54321})
    
    def test_comprimento(self):
        response = self.client.post('/words-length?frase=Esta é uma frase de teste.')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"comprimento médio": 3.3})
    
    def test_palavras(self):
        response = self.client.post('words?frase1=Esta é uma frase de teste.&frase2=Esta é outra frase de teste.')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "palavras em comum": ["uma", "frase", "de", 'outra'],
            "palavras diferentes": ["Esta", "é", "teste."]
        })