import pytest
from imposto import *


# ------------------------
# imposto bruto
# ------------------------

def test_imposto_isento():
    assert calcular_imposto_bruto(2000) == 0


def test_imposto_zero():
    assert calcular_imposto_bruto(0) == 0


def test_imposto_limite_superior_faixa1():
    assert calcular_imposto_bruto(1999) == 0


def test_imposto_limite_inferior_faixa2():
    assert calcular_imposto_bruto(2001) == 2001 * 0.15


def test_imposto_faixa_media():
    assert calcular_imposto_bruto(3000) == 450


def test_imposto_limite_superior_faixa2():
    assert calcular_imposto_bruto(5000) == 5000 * 0.15


def test_imposto_limite_inferior_faixa3():
    assert calcular_imposto_bruto(5001) == 5001 * 0.27


def test_imposto_faixa_alta():
    assert calcular_imposto_bruto(6000) == 1620


def test_renda_negativa():
    with pytest.raises(ValueError):
        calcular_imposto_bruto(-1)


# ------------------------
# deducao dependentes
# ------------------------

def test_sem_dependentes():
    assert calcular_deducao_dependentes(0) == 0


def test_um_dependente():
    assert calcular_deducao_dependentes(1) == 100


def test_varios_dependentes():
    assert calcular_deducao_dependentes(3) == 300


def test_muitos_dependentes():
    assert calcular_deducao_dependentes(10) == 1000


def test_dependentes_negativo():
    with pytest.raises(ValueError):
        calcular_deducao_dependentes(-1)


# ------------------------
# imposto liquido
# ------------------------

def test_imposto_liquido_sem_dependentes():
    assert calcular_imposto_liquido(4000, 0) == 600


def test_imposto_liquido_com_dependentes():
    assert calcular_imposto_liquido(4000, 2) == 400


def test_imposto_liquido_nao_negativo():
    assert calcular_imposto_liquido(2100, 10) == 0


def test_imposto_liquido_limite_isencao():
    assert calcular_imposto_liquido(2000, 1) == 0


def test_imposto_liquido_renda_alta():
    assert calcular_imposto_liquido(10000, 1) == (10000 * 0.27) - 100


def test_imposto_liquido_dependentes_zero():
    assert calcular_imposto_liquido(3000, 0) == 450


# ------------------------
# salario liquido
# ------------------------

def test_salario_liquido_sem_imposto():
    assert salario_liquido(2000, 0) == 2000


def test_salario_liquido_com_imposto():
    assert salario_liquido(4000, 0) == 3400


def test_salario_liquido_com_dependentes():
    assert salario_liquido(4000, 2) == 3600


def test_salario_liquido_grande_deducao():
    assert salario_liquido(2500, 20) == 2500


def test_salario_liquido_renda_alta():
    imposto = calcular_imposto_liquido(8000, 2)
    assert salario_liquido(8000, 2) == 8000 - imposto


# ------------------------
# isencao
# ------------------------

def test_isento_true():
    assert esta_isento(2000) is True


def test_isento_false():
    assert esta_isento(3000) is False


def test_isento_limite():
    assert esta_isento(1999) is True


def test_isento_2001():
    assert esta_isento(2001) is False


def test_isento_zero():
    assert esta_isento(0) is True


# ------------------------
# testes extras importantes
# ------------------------

def test_imposto_fronteira_1998():
    assert calcular_imposto_bruto(1998) == 0


def test_imposto_fronteira_2002():
    assert calcular_imposto_bruto(2002) == 2002 * 0.15


def test_imposto_fronteira_4999():
    assert calcular_imposto_bruto(4999) == 4999 * 0.15


def test_imposto_fronteira_5002():
    assert calcular_imposto_bruto(5002) == 5002 * 0.27