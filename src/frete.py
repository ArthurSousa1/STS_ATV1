def calcular_frete(peso: float, destino: str, valor_pedido: float) -> float:
    if peso <= 0:
        raise ValueError("Peso inválido")

    if destino not in ["mesma_regiao", "outra_regiao", "internacional"]:
        raise ValueError("Destino inválido")

    if valor_pedido < 0:
        raise ValueError("Valor do pedido inválido")

    if peso <= 1:
        frete = 10.0
    elif peso <= 5:
        frete = 15.0
    elif peso <= 20:
        frete = 25.0
    else:
        raise ValueError("Peso não permitido")

    if destino == "outra_regiao":
        frete *= 1.5   
    elif destino == "internacional":
        frete *= 2 

    if valor_pedido > 200:
        return 0.0

    return frete