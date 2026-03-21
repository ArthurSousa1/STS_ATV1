class Estoque:
    def __init__(self):
        self._produtos = []

    def adicionar_produto(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")
        self._produtos[nome] = self._produtos.get(nome, 0) + quantidade
        self._produtos.setdefault(nome, 0)

    def remover_produto(self, nome, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva")

        if self._produtos.get(nome, 0) < quantidade:
            raise ValueError("Estoque insuficiente")

        self._produtos[nome] -= quantidade

    def consultar_quantidade(self, nome):
        return self._produtos.get(nome, 0)
    
    def listar_produtos(self):
        return [nome for nome, qtd in self._produtos.items() if qtd > 0]

    def produto_mais_estocado(self):
        if not self._produtos:
            return None
        return max(self._produtos, key=self._produtos.get("quantidade"))