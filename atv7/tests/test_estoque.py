import unittest
from src.estoque import Estoque

class TestEstoque(unittest.TestCase):

    def test_adicionar_produto_novo(self):
        estoque = Estoque()
        estoque.adicionar_produto("banana", 10)
        self.assertEqual(estoque.consultar_quantidade("banana"), 10)

    def test_adicionar_produto_existente_incrementa(self):
        estoque = Estoque()
        estoque.adicionar_produto("banana", 10)
        estoque.adicionar_produto("banana", 5)
        self.assertEqual(estoque.consultar_quantidade("banana"), 15)

    def test_adicionar_quantidade_invalida(self):
        estoque = Estoque()
        with self.assertRaises(ValueError):
            estoque.adicionar_produto("banana", 0)

# =========================
    def test_remover_produto(self):
        estoque = Estoque()
        estoque.adicionar_produto("banana", 10)
        estoque.remover_produto("banana", 4)
        self.assertEqual(estoque.consultar_quantidade("banana"), 6)

    def test_remover_quantidade_maior_que_estoque(self):
        estoque = Estoque()
        estoque.adicionar_produto("banana", 5)
        with self.assertRaises(ValueError):
            estoque.remover_produto("banana", 10)

    def test_remover_quantidade_invalida(self):
        estoque = Estoque()
        estoque.adicionar_produto("banana", 5)
        with self.assertRaises(ValueError):
            estoque.remover_produto("banana", 0)

# =========================
    def test_consultar_produto_existente(self):
        estoque = Estoque()
        estoque.adicionar_produto("banana", 10)
        self.assertEqual(estoque.consultar_quantidade("banana"), 10)

    def test_consultar_produto_inexistente(self):
        estoque = Estoque()
        self.assertEqual(estoque.consultar_quantidade("maçã"), 0)

# =========================
    def test_listar_produtos(self):
        estoque = Estoque()
        estoque.adicionar_produto("banana", 10) 
        self.assertIn("banana", estoque.listar_produtos())

    def test_produto_mais_estocado(self):
        estoque = Estoque()
        estoque.adicionar_produto("banana", 20)
        estoque.adicionar_produto("maçã", 10)
        self.assertEqual(estoque.produto_mais_estocado(), "banana")

    def test_produto_mais_estocado_vazio(self):
        estoque = Estoque()
        self.assertIsNone(estoque.produto_mais_estocado())


if __name__ == "__main__":
    unittest.main()