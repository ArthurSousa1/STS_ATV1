from unittest.mock import MagicMock
import unittest

from src.calculadora import Calculadora

## ------------------------
## Teste de Entrada e Saída
## ------------------------
class TestEntradaSaida(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock()
        self.calc = Calculadora(self.repo)

## Soma
    def test_soma_retorna_valor_correto(self):
        resultado = self.calc.somar(5, 3)
        self.assertEqual(resultado, 8)

    def test_soma_atualiza_ultimo_resultado(self):
        self.calc.somar(5, 3)
        self.assertEqual(self.calc.obter_ultimo_resultado(), 8)

## Subtrair
    def test_subtrair_retorna_valor_correto(self):
        resultado = self.calc.subtrair(5, 3)
        self.assertEqual(resultado, 2)

## Multiplicar
    def test_multiplicar_retorna_valor_correto(self):
        resultado = self.calc.multiplicar(5, 3)
        self.assertEqual(resultado, 15)

## Dividir
    def test_dividir_retorna_valor_correto(self):
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5)

## Potencia
    def test_potencia_retorna_valor_correto(self):
        resultado = self.calc.potencia(2, 2)
        self.assertEqual(resultado, 4)

## ------------------------
## Teste de Tipagem
## ------------------------
    def test_tipagem_string_rejeita(self):
        with self.assertRaises(TypeError):
            self.calc.somar("5", 3)
    
    def test_tipagem_nome_rejeitado(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)

## ------------------------
## Teste de Limites
## ------------------------
    def test_limite_zero(self):
        self.assertEqual(self.calc.somar(0, 5), 5)

    def test_limite_pequeno(self):
        self.assertAlmostEqual(self.calc.multiplicar(-1e-10, 2), -2e-10)

    def test_limite_floar_grande(self):
        import sys
        grande = sys.float_info.max / 2
        resultado = self.calc. somar(grande, grande)
        self.assertFalse(resultado == float('inf')) # Não deve transbordar

## ------------------------
## Teste de Valores fora do intervalo
## ------------------------
    def test_divisao_por_zero_levanta_excecao(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

## ------------------------
## Teste de Mensagens de erro
## ------------------------

    def test_mensagem_divisao_por_zero(self):
        with self.assertRaisesRegex(ValueError, "Divisão por zero"):
            self.calc.dividir(5, 0)

    def test_mensagem_tipo_invalido(self):
        with self.assertRaisesRegex(TypeError, "Argumentos devem ser números"):
            self.calc.somar("x", 1)

## ------------------------
## Teste de Fluxo de Controle
## ------------------------
    def test_caminho_divisao_normal(self):
        self.assertEqual(self.calc.dividir(10, 2), 5.0)

    def test_caminho_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)