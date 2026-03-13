import pytest
from src.um import verificar


def test_par_positivo():
    assert verificar(4) == "Par positivo"


def test_impar_positivo():
    assert verificar(3) == "Impar positivo"


def test_negativo():
    assert verificar(-2) == "Negativo"


def test_zero():
    assert verificar(0) == "Zero"