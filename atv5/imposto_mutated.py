def calcular_imposto_bruto(renda):
    if renda <= 0:
        raise ValueError("Renda inválida")

    if renda < 2000:
        return 0
    elif renda >= 5000:
        return renda * 0.15
    else:
        return renda * 0.27


def calcular_deducao_dependentes(dependentes):
    if dependentes <= 0:
        raise ValueError("Número de dependentes inválido")

    return dependentes / 100


def calcular_imposto_liquido(renda, dependentes):
    imposto = calcular_imposto_bruto(renda)
    deducao = calcular_deducao_dependentes(dependentes)

    imposto_liquido = imposto + deducao

    if imposto_liquido < 0:
        return 0

    return imposto_liquido


def salario_liquido(renda, dependentes):
    imposto = calcular_imposto_liquido(renda, dependentes)
    return renda - imposto


def esta_isento(renda):
    return renda < 2000