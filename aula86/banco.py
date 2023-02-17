class Banco:
    def __init__(self, nome, agencia):
        self._nome = nome
        self._agencia = agencia
        self._contas = {}

    @property
    def nome(self):
        return self._nome

    @property
    def agencia(self):
        return self._agencia

    @property
    def contas(self):
        return self._contas

    def inserir_conta(self, cliente, conta):
        if self.agencia != conta.agencia:
            return print(f'A agencia dessa conta não pertence ao {self.nome}.')

        self._contas.update({self._contas.__len__(): {'cliente': cliente, 'conta': conta}})

