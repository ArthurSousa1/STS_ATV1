import pytest
from src.cpf import validar_cpf, formatar_cpf

@pytest.fixture
def cpfs_validos():
    """Lista de CPFs válidos"""
    return [
        "52998224725",    
        "12345678909",    
        "11144477735",    
        "00000000191",    
    ]

@pytest.fixture
def cpfs_invalidos():
    """Lista de CPFs inválidos"""
    return [
        "11111111111",    
        "12345678900",    
        "1234567890",     
        "123456789000",   
        "abc12345678",    
        "",               
        None,             
    ]

def test_validar_cpf_valido(cpfs_validos):
    lista = cpfs_validos
    for cpf in lista:
        assert validar_cpf(cpf) is True


def test_validar_cpf_invalido(cpfs_invalidos):
    lista = cpfs_invalidos
    for cpf in lista:
        assert validar_cpf(cpf) is False


@pytest.mark.parametrize("cpf, esperado", [
    ("52998224725", True),
    ("11111111111", False),
    ("1234567890", False),
], ids=["valido_exemplo", "todos_iguais", "validador_errado"])

def test_validar_cpf_parametrizado(cpf, esperado):
    resultado = validar_cpf(cpf)
    assert resultado is esperado

def test_validar_cpf_com_letras(cpfs_invalidos):
    cpf = cpfs_invalidos[4]
    resultado = validar_cpf(cpf)
    assert resultado is False

def test_validar_cpf_none(cpfs_invalidos):
    cpf = cpfs_invalidos[6]
    resultado = validar_cpf(cpf)
    assert resultado is False

def test_validar_cpf_string_vazia(cpfs_invalidos):
    cpf = cpfs_invalidos[5]
    resultado = validar_cpf(cpf)
    assert resultado is False


def test_formatar_cpf_valido(cpfs_validos):
    cpf = cpfs_validos[0]  
    resultado = formatar_cpf(cpf)
    assert resultado == "529.982.247-25"


def test_formatar_cpf_valido_com_zeros(cpfs_validos):
    cpf = cpfs_validos[3] 
    resultado = formatar_cpf(cpf)
    assert resultado == "000.000.001-91"

def test_formatar_cpf_invalido_levanta_excecao(cpfs_invalidos):
    lista = cpfs_invalidos
    for cpf in lista:
        with pytest.raises(ValueError):
            formatar_cpf(cpf)
