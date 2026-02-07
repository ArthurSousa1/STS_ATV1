def validar_nota(nota):
    """
    Valida se a nota está no intervalo [0, 10].
    """
    try:
        return 0 <= nota <= 10
    except TypeError:
        return False


def calcular_media(notas):
    """
    Calcula a média das notas válidas.
    Ignora notas inválidas.
    """
    if not notas:
        raise ValueError("Lista de notas vazia")

    notas_validas = [n for n in notas if validar_nota(n)]

    if not notas_validas:
        raise ValueError("Nenhuma nota válida")

    return sum(notas_validas) / len(notas_validas)


def obter_situacao(media):
    """
    Determina a situação do aluno com base na média.
    """
    if media < 0 or media > 10:
        raise ValueError("Média inválida")

    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"


def calcular_estatisticas(notas):
    """
    Calcula estatísticas das notas.
    """
    notas_validas = [n for n in notas if validar_nota(n)]

    if not notas_validas:
        raise ValueError("Nenhuma nota válida")

    media = calcular_media(notas_validas)

    estatisticas = {
        "media": media,
        "maior": max(notas_validas),
        "menor": min(notas_validas),
        "aprovados": 0,
        "recuperacao": 0,
        "reprovados": 0
    }

    for nota in notas_validas:
        situacao = obter_situacao(nota)
        if situacao == "Aprovado":
            estatisticas["aprovados"] += 1
        elif situacao == "Recuperação":
            estatisticas["recuperacao"] += 1
        else:
            estatisticas["reprovados"] += 1

    return estatisticas


def normalizar_notas(notas, nota_maxima=10):
    """
    Normaliza as notas para a escala 0–10.
    """
    if nota_maxima <= 0:
        raise ValueError("Nota máxima inválida")

    return [(nota / nota_maxima) * 10 for nota in notas]
