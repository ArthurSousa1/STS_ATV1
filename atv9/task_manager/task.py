from enum import IntEnum, Enum
from datetime import datetime


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


class Task:
    def __init__(self, id, titulo, descricao, prioridade, prazo):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.prazo = prazo
        self.status = Status.PENDENTE

    def validar(self):
        if len(self.titulo) < 3:
            raise ValueError("Título inválido")

        if self.prazo < datetime.now():
            raise ValueError("Prazo no passado")

    def atualizar_status(self, novo_status):
        if not isinstance(novo_status, Status):
            raise ValueError("Status inválido")

        self.status = novo_status