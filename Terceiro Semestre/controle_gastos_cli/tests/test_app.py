import tempfile
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import adicionar, carregar, salvar, total


class TestApp(unittest.TestCase):
    def test_adiciona_gasto(self):
        gastos = []

        adicionar(gastos, "Mercado", 25.5)

        self.assertEqual(gastos, [{"descricao": "Mercado", "valor": 25.5}])

    def test_soma_total(self):
        gastos = []

        adicionar(gastos, "Mercado", 10)
        adicionar(gastos, "Internet", 15.9)

        self.assertEqual(total(gastos), 25.9)

    def test_salva_e_carrega(self):
        gastos = []
        adicionar(gastos, "Luz", 99.9)

        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "dados.json"
            salvar(gastos, caminho)

            self.assertEqual(carregar(caminho), gastos)

    def test_rejeita_gasto_invalido(self):
        with self.assertRaises(ValueError):
            adicionar([], "", 10)

    def test_buscar_cotacao_dolar(self):
        from main import buscar_cotacao_dolar
        cotacao = buscar_cotacao_dolar()
        if cotacao is not None:
            self.assertIsInstance(cotacao, float)
            self.assertGreater(cotacao, 0)

if __name__ == "__main__":
    unittest.main()
