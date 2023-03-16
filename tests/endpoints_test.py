import unittest
from fastapi.testclient import TestClient
from app.main import app

class TestInvertNumber(unittest.TestCase):
    
    def setUp(self):
        self.client = TestClient(app)
    
    def test_inverter_digitos_positivos(self):
        response = self.client.get("/reverse-int/231")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"numero invertido": 132})
    
    def test_inverter_digitos_negativos(self):
        response = self.client.get("/reverse-int/-12345")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"numero invertido": -54321})
    
    def test_comprimento(self):
        response = self.client.post('/words-length?frase=Esta é uma frase de teste.')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"comprimento médio": 3.3})
    
    def test_palavras(self):
        response = self.client.post("/words?frase1=hello%20world&frase2=goodbye%20world")
        expected = {
            "palavras em comum": ["world"],
            "palavras diferentes": ["goodbye", "hello"]
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)