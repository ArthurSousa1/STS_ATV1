from src.dois import classificar

def test_alto():
    assert classificar(101) == "Alto"

def test_medio():
    assert classificar(51) == "Medio"

def test_baixo():
    assert classificar(49) == "Baixo"