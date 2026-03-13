from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
def calcular_imposto_bruto(renda):
    args = [renda]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_calcular_imposto_bruto__mutmut_orig, x_calcular_imposto_bruto__mutmut_mutants, args, kwargs, None)
def x_calcular_imposto_bruto__mutmut_orig(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_1(renda):
    if renda <= 0:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_2(renda):
    if renda < 1:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_3(renda):
    if renda < 0:
        raise ValueError(None)

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_4(renda):
    if renda < 0:
        raise ValueError("XXRenda inválidaXX")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_5(renda):
    if renda < 0:
        raise ValueError("renda inválida")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_6(renda):
    if renda < 0:
        raise ValueError("RENDA INVÁLIDA")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_7(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda < 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_8(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda <= 2001:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_9(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 1
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_10(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 0
    elif renda < 5000:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_11(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 0
    elif renda <= 5001:
        return renda * 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_12(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda / 0.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_13(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 1.15
    else:
        return renda * 0.27
def x_calcular_imposto_bruto__mutmut_14(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda / 0.27
def x_calcular_imposto_bruto__mutmut_15(renda):
    if renda < 0:
        raise ValueError("Renda inválida")

    if renda <= 2000:
        return 0
    elif renda <= 5000:
        return renda * 0.15
    else:
        return renda * 1.27

x_calcular_imposto_bruto__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_calcular_imposto_bruto__mutmut_1': x_calcular_imposto_bruto__mutmut_1, 
    'x_calcular_imposto_bruto__mutmut_2': x_calcular_imposto_bruto__mutmut_2, 
    'x_calcular_imposto_bruto__mutmut_3': x_calcular_imposto_bruto__mutmut_3, 
    'x_calcular_imposto_bruto__mutmut_4': x_calcular_imposto_bruto__mutmut_4, 
    'x_calcular_imposto_bruto__mutmut_5': x_calcular_imposto_bruto__mutmut_5, 
    'x_calcular_imposto_bruto__mutmut_6': x_calcular_imposto_bruto__mutmut_6, 
    'x_calcular_imposto_bruto__mutmut_7': x_calcular_imposto_bruto__mutmut_7, 
    'x_calcular_imposto_bruto__mutmut_8': x_calcular_imposto_bruto__mutmut_8, 
    'x_calcular_imposto_bruto__mutmut_9': x_calcular_imposto_bruto__mutmut_9, 
    'x_calcular_imposto_bruto__mutmut_10': x_calcular_imposto_bruto__mutmut_10, 
    'x_calcular_imposto_bruto__mutmut_11': x_calcular_imposto_bruto__mutmut_11, 
    'x_calcular_imposto_bruto__mutmut_12': x_calcular_imposto_bruto__mutmut_12, 
    'x_calcular_imposto_bruto__mutmut_13': x_calcular_imposto_bruto__mutmut_13, 
    'x_calcular_imposto_bruto__mutmut_14': x_calcular_imposto_bruto__mutmut_14, 
    'x_calcular_imposto_bruto__mutmut_15': x_calcular_imposto_bruto__mutmut_15
}
x_calcular_imposto_bruto__mutmut_orig.__name__ = 'x_calcular_imposto_bruto'


def calcular_deducao_dependentes(dependentes):
    args = [dependentes]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_calcular_deducao_dependentes__mutmut_orig, x_calcular_deducao_dependentes__mutmut_mutants, args, kwargs, None)


def x_calcular_deducao_dependentes__mutmut_orig(dependentes):
    if dependentes < 0:
        raise ValueError("Número de dependentes inválido")

    return dependentes * 100


def x_calcular_deducao_dependentes__mutmut_1(dependentes):
    if dependentes <= 0:
        raise ValueError("Número de dependentes inválido")

    return dependentes * 100


def x_calcular_deducao_dependentes__mutmut_2(dependentes):
    if dependentes < 1:
        raise ValueError("Número de dependentes inválido")

    return dependentes * 100


def x_calcular_deducao_dependentes__mutmut_3(dependentes):
    if dependentes < 0:
        raise ValueError(None)

    return dependentes * 100


def x_calcular_deducao_dependentes__mutmut_4(dependentes):
    if dependentes < 0:
        raise ValueError("XXNúmero de dependentes inválidoXX")

    return dependentes * 100


def x_calcular_deducao_dependentes__mutmut_5(dependentes):
    if dependentes < 0:
        raise ValueError("número de dependentes inválido")

    return dependentes * 100


def x_calcular_deducao_dependentes__mutmut_6(dependentes):
    if dependentes < 0:
        raise ValueError("NÚMERO DE DEPENDENTES INVÁLIDO")

    return dependentes * 100


def x_calcular_deducao_dependentes__mutmut_7(dependentes):
    if dependentes < 0:
        raise ValueError("Número de dependentes inválido")

    return dependentes / 100


def x_calcular_deducao_dependentes__mutmut_8(dependentes):
    if dependentes < 0:
        raise ValueError("Número de dependentes inválido")

    return dependentes * 101

x_calcular_deducao_dependentes__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_calcular_deducao_dependentes__mutmut_1': x_calcular_deducao_dependentes__mutmut_1, 
    'x_calcular_deducao_dependentes__mutmut_2': x_calcular_deducao_dependentes__mutmut_2, 
    'x_calcular_deducao_dependentes__mutmut_3': x_calcular_deducao_dependentes__mutmut_3, 
    'x_calcular_deducao_dependentes__mutmut_4': x_calcular_deducao_dependentes__mutmut_4, 
    'x_calcular_deducao_dependentes__mutmut_5': x_calcular_deducao_dependentes__mutmut_5, 
    'x_calcular_deducao_dependentes__mutmut_6': x_calcular_deducao_dependentes__mutmut_6, 
    'x_calcular_deducao_dependentes__mutmut_7': x_calcular_deducao_dependentes__mutmut_7, 
    'x_calcular_deducao_dependentes__mutmut_8': x_calcular_deducao_dependentes__mutmut_8
}
x_calcular_deducao_dependentes__mutmut_orig.__name__ = 'x_calcular_deducao_dependentes'


def calcular_imposto_liquido(renda, dependentes):
    args = [renda, dependentes]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_calcular_imposto_liquido__mutmut_orig, x_calcular_imposto_liquido__mutmut_mutants, args, kwargs, None)


def x_calcular_imposto_liquido__mutmut_orig(renda, dependentes):
    imposto = calcular_imposto_bruto(renda)
    deducao = calcular_deducao_dependentes(dependentes)

    imposto_liquido = imposto - deducao

    if imposto_liquido < 0:
        return 0

    return imposto_liquido


def x_calcular_imposto_liquido__mutmut_1(renda, dependentes):
    imposto = None
    deducao = calcular_deducao_dependentes(dependentes)

    imposto_liquido = imposto - deducao

    if imposto_liquido < 0:
        return 0

    return imposto_liquido


def x_calcular_imposto_liquido__mutmut_2(renda, dependentes):
    imposto = calcular_imposto_bruto(None)
    deducao = calcular_deducao_dependentes(dependentes)

    imposto_liquido = imposto - deducao

    if imposto_liquido < 0:
        return 0

    return imposto_liquido


def x_calcular_imposto_liquido__mutmut_3(renda, dependentes):
    imposto = calcular_imposto_bruto(renda)
    deducao = None

    imposto_liquido = imposto - deducao

    if imposto_liquido < 0:
        return 0

    return imposto_liquido


def x_calcular_imposto_liquido__mutmut_4(renda, dependentes):
    imposto = calcular_imposto_bruto(renda)
    deducao = calcular_deducao_dependentes(None)

    imposto_liquido = imposto - deducao

    if imposto_liquido < 0:
        return 0

    return imposto_liquido


def x_calcular_imposto_liquido__mutmut_5(renda, dependentes):
    imposto = calcular_imposto_bruto(renda)
    deducao = calcular_deducao_dependentes(dependentes)

    imposto_liquido = None

    if imposto_liquido < 0:
        return 0

    return imposto_liquido


def x_calcular_imposto_liquido__mutmut_6(renda, dependentes):
    imposto = calcular_imposto_bruto(renda)
    deducao = calcular_deducao_dependentes(dependentes)

    imposto_liquido = imposto + deducao

    if imposto_liquido < 0:
        return 0

    return imposto_liquido


def x_calcular_imposto_liquido__mutmut_7(renda, dependentes):
    imposto = calcular_imposto_bruto(renda)
    deducao = calcular_deducao_dependentes(dependentes)

    imposto_liquido = imposto - deducao

    if imposto_liquido <= 0:
        return 0

    return imposto_liquido


def x_calcular_imposto_liquido__mutmut_8(renda, dependentes):
    imposto = calcular_imposto_bruto(renda)
    deducao = calcular_deducao_dependentes(dependentes)

    imposto_liquido = imposto - deducao

    if imposto_liquido < 1:
        return 0

    return imposto_liquido


def x_calcular_imposto_liquido__mutmut_9(renda, dependentes):
    imposto = calcular_imposto_bruto(renda)
    deducao = calcular_deducao_dependentes(dependentes)

    imposto_liquido = imposto - deducao

    if imposto_liquido < 0:
        return 1

    return imposto_liquido

x_calcular_imposto_liquido__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_calcular_imposto_liquido__mutmut_1': x_calcular_imposto_liquido__mutmut_1, 
    'x_calcular_imposto_liquido__mutmut_2': x_calcular_imposto_liquido__mutmut_2, 
    'x_calcular_imposto_liquido__mutmut_3': x_calcular_imposto_liquido__mutmut_3, 
    'x_calcular_imposto_liquido__mutmut_4': x_calcular_imposto_liquido__mutmut_4, 
    'x_calcular_imposto_liquido__mutmut_5': x_calcular_imposto_liquido__mutmut_5, 
    'x_calcular_imposto_liquido__mutmut_6': x_calcular_imposto_liquido__mutmut_6, 
    'x_calcular_imposto_liquido__mutmut_7': x_calcular_imposto_liquido__mutmut_7, 
    'x_calcular_imposto_liquido__mutmut_8': x_calcular_imposto_liquido__mutmut_8, 
    'x_calcular_imposto_liquido__mutmut_9': x_calcular_imposto_liquido__mutmut_9
}
x_calcular_imposto_liquido__mutmut_orig.__name__ = 'x_calcular_imposto_liquido'


def salario_liquido(renda, dependentes):
    args = [renda, dependentes]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_salario_liquido__mutmut_orig, x_salario_liquido__mutmut_mutants, args, kwargs, None)


def x_salario_liquido__mutmut_orig(renda, dependentes):
    imposto = calcular_imposto_liquido(renda, dependentes)
    return renda - imposto


def x_salario_liquido__mutmut_1(renda, dependentes):
    imposto = None
    return renda - imposto


def x_salario_liquido__mutmut_2(renda, dependentes):
    imposto = calcular_imposto_liquido(None, dependentes)
    return renda - imposto


def x_salario_liquido__mutmut_3(renda, dependentes):
    imposto = calcular_imposto_liquido(renda, None)
    return renda - imposto


def x_salario_liquido__mutmut_4(renda, dependentes):
    imposto = calcular_imposto_liquido(dependentes)
    return renda - imposto


def x_salario_liquido__mutmut_5(renda, dependentes):
    imposto = calcular_imposto_liquido(renda, )
    return renda - imposto


def x_salario_liquido__mutmut_6(renda, dependentes):
    imposto = calcular_imposto_liquido(renda, dependentes)
    return renda + imposto

x_salario_liquido__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_salario_liquido__mutmut_1': x_salario_liquido__mutmut_1, 
    'x_salario_liquido__mutmut_2': x_salario_liquido__mutmut_2, 
    'x_salario_liquido__mutmut_3': x_salario_liquido__mutmut_3, 
    'x_salario_liquido__mutmut_4': x_salario_liquido__mutmut_4, 
    'x_salario_liquido__mutmut_5': x_salario_liquido__mutmut_5, 
    'x_salario_liquido__mutmut_6': x_salario_liquido__mutmut_6
}
x_salario_liquido__mutmut_orig.__name__ = 'x_salario_liquido'


def esta_isento(renda):
    args = [renda]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_esta_isento__mutmut_orig, x_esta_isento__mutmut_mutants, args, kwargs, None)


def x_esta_isento__mutmut_orig(renda):
    return renda <= 2000


def x_esta_isento__mutmut_1(renda):
    return renda < 2000


def x_esta_isento__mutmut_2(renda):
    return renda <= 2001

x_esta_isento__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_esta_isento__mutmut_1': x_esta_isento__mutmut_1, 
    'x_esta_isento__mutmut_2': x_esta_isento__mutmut_2
}
x_esta_isento__mutmut_orig.__name__ = 'x_esta_isento'