import pytest
from hypothesis import given, strategies as st
from src.frete import calcular_frete

@pytest.fixture
def destinos_validos():
    return ["mesma_regiao", "outra_regiao", "internacional"]

@pytest.mark.parametrize("peso, esperado", [
    (0.5, 10.0), 
    (3, 15.0),     
    (10, 25.0),   
])
def test_classes_equivalencia_peso(peso, esperado):
    assert calcular_frete(peso, "mesma_regiao", 100) == esperado

def test_classe_equivalencia_frete_gratis():
    assert calcular_frete(3, "mesma_regiao", 250) == 0.0

@pytest.mark.parametrize("peso, esperado", [
    (0.99, 10.0),
    (1.0, 10.0),
    (1.01, 15.0),

    (4.99, 15.0),
    (5.0, 15.0),
    (5.01, 25.0),

    (19.99, 25.0),
    (20.0, 25.0),
])
def test_valores_limite_validos(peso, esperado):
    assert calcular_frete(peso, "mesma_regiao", 100) == esperado

def test_valor_limite_acima_20():
    with pytest.raises(ValueError):
        calcular_frete(20.01, "mesma_regiao", 100)

@pytest.mark.parametrize("peso, destino, esperado", [
    (1, "mesma_regiao", 10.0),
    (1, "outra_regiao", 15.0),
    (1, "internacional", 20.0),
    (10, "mesma_regiao", 25.0),
    (10, "outra_regiao", 37.5),
    (10, "internacional", 50.0),
])
def test_tabela_decisao(peso, destino, esperado):
    assert calcular_frete(peso, destino, 100) == esperado

def test_peso_invalido():
    with pytest.raises(ValueError):
        calcular_frete(0, "mesma_regiao", 100)

def test_destino_invalido():
    with pytest.raises(ValueError):
        calcular_frete(1, "invalido", 100)

@given(
    peso=st.floats(min_value=0.01, max_value=20),
    valor=st.floats(min_value=0, max_value=200),
)
def test_frete_nunca_negativo(peso, valor):
    frete = calcular_frete(peso, "mesma_regiao", valor)
    assert frete >= 0

@given(
    peso=st.floats(min_value=0.01, max_value=20),
)
def test_frete_gratis_acima_200(peso):
    assert calcular_frete(peso, "internacional", 201) == 0.0

@given(
    peso=st.floats(min_value=0.01, max_value=20),
    valor=st.floats(min_value=0, max_value=200),
)
def test_outra_regiao_maior_ou_igual_mesma(peso, valor):
    frete_mesma = calcular_frete(peso, "mesma_regiao", valor)
    frete_outra = calcular_frete(peso, "outra_regiao", valor)
    assert frete_outra >= frete_mesma