import pytest
from src.avaliador import (
    validar_nota,
    calcular_media,
    obter_situacao,
    calcular_estatisticas,
    normalizar_notas
)

# ==================================================
# Testes: validar_nota (8 testes)
# ==================================================

class TestValidarNota:

    def test_nota_valida_zero(self):
        assert validar_nota(0) is True

    def test_nota_valida_dez(self):
        assert validar_nota(10) is True

    def test_nota_valida_decimal(self):
        assert validar_nota(7.5) is True

    def test_nota_negativa(self):
        assert validar_nota(-1) is False

    def test_nota_acima_limite(self):
        assert validar_nota(11) is False

    def test_nota_decimal_acima(self):
        assert validar_nota(10.1) is False

    def test_tipo_string(self):
        assert validar_nota("7") is False

    def test_tipo_none(self):
        assert validar_nota(None) is False


# ==================================================
# Testes: calcular_media (6 testes)
# ==================================================

class TestCalcularMedia:

    def test_media_tres_notas(self):
        assert calcular_media([5, 7, 9]) == pytest.approx(7.0)

    def test_media_com_decimal(self):
        assert calcular_media([6.5, 7.5]) == pytest.approx(7.0)

    def test_media_ignora_invalidas(self):
        assert calcular_media([5, -1, 7, 11]) == pytest.approx(6.0)

    def test_media_uma_nota_valida(self):
        assert calcular_media([8]) == pytest.approx(8.0)

    def test_lista_vazia(self):
        with pytest.raises(ValueError):
            calcular_media([])

    def test_sem_notas_validas(self):
        with pytest.raises(ValueError):
            calcular_media([-1, 20, 30])


# ==================================================
# Testes: obter_situacao (6 testes)
# ==================================================

class TestObterSituacao:

    def test_aprovado_limite(self):
        assert obter_situacao(7.0) == "Aprovado"

    def test_aprovado_alto(self):
        assert obter_situacao(9.8) == "Aprovado"

    def test_recuperacao_limite(self):
        assert obter_situacao(5.0) == "Recuperação"

    def test_recuperacao_meio(self):
        assert obter_situacao(6.5) == "Recuperação"

    def test_reprovado(self):
        assert obter_situacao(4.9) == "Reprovado"

    def test_media_invalida(self):
        with pytest.raises(ValueError):
            obter_situacao(11)


# ==================================================
# Testes: calcular_estatisticas (6 testes)
# ==================================================

class TestCalcularEstatisticas:

    def test_estatisticas_basicas(self):
        notas = [3, 5, 7, 9]
        r = calcular_estatisticas(notas)

        assert r["media"] == pytest.approx(6.0)
        assert r["maior"] == 9
        assert r["menor"] == 3
        assert r["aprovados"] == 2
        assert r["recuperacao"] == 1
        assert r["reprovados"] == 1

    def test_estatisticas_com_invalidas(self):
        notas = [3, -1, 5, 11, 8]
        r = calcular_estatisticas(notas)

        assert r["maior"] == 8
        assert r["menor"] == 3

    def test_estatisticas_todas_aprovadas(self):
        notas = [7, 8, 9]
        r = calcular_estatisticas(notas)

        assert r["aprovados"] == 3
        assert r["reprovados"] == 0
        assert r["recuperacao"] == 0

    def test_estatisticas_todas_reprovadas(self):
        notas = [1, 2, 3]
        r = calcular_estatisticas(notas)

        assert r["reprovados"] == 3

    def test_estatisticas_com_uma_nota(self):
        notas = [10]
        r = calcular_estatisticas(notas)

        assert r["media"] == 10
        assert r["aprovados"] == 1

    def test_estatisticas_sem_validas(self):
        with pytest.raises(ValueError):
            calcular_estatisticas([-5, 20])


# ==================================================
# Testes: normalizar_notas (4 testes)
# ==================================================

class TestNormalizarNotas:

    def test_normalizacao_padrao(self):
        assert normalizar_notas([5, 10]) == [5.0, 10.0]

    def test_normalizacao_customizada(self):
        assert normalizar_notas([10, 20], 20) == [5.0, 10.0]

    def test_normalizacao_com_decimal(self):
        assert normalizar_notas([5, 15], 20) == [2.5, 7.5]

    def test_nota_maxima_invalida(self):
        with pytest.raises(ValueError):
            normalizar_notas([5, 10], 0)
