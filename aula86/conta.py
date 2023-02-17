from abc import abstractmethod


class Conta:
    def __init__(self, agencia, numero, saldo=0):
        self._agencia = agencia
        self._numero = numero
        self._saldo = float(saldo)

    @property
    def agencia(self):
        return self._agencia

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        """
        Realiza um depósito na conta do cliente.

        :param saldo: int, float
        :return: print('Valor depositado com sucesso!')
        """
        if valor <= 0:
            return print('Você não pode depositar um valor menor que 0.')

        if not str(valor).isnumeric():
            return print('O valor do depósito deve ser um número.')

        self._saldo += valor
        return print('Valor depositado com sucesso!')

    @abstractmethod
    def sacar(self, banco, cliente, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo=0):
        super().__init__(agencia, numero, saldo)

    def depositar(self, saldo):
        if saldo > 1000:
            return print('Contas Correntes não podem depositar valor acima de R$ 1000,00')

        super().depositar(saldo)

    def sacar(self, banco, cliente, valor):
        if banco.agencia != self.agencia:
            return print(f'Essa conta não pertence ao banco {banco.nome}')

        for conta in banco.contas.values():
            if self == conta['conta'] and cliente == conta['cliente']:
                if valor > self.saldo:
                    return print(f'Você pode sacar até: R${float(self.saldo):.2f}.')

                if valor > 1000:
                    return print('Você não pode sacar mais que R$1000,00.')

                self._saldo -= valor

                return print(f'Saque realizado com sucesso! Seu novo saldo: {self.saldo}')

        return print('Esse cliente não pertence a esse banco.')


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero, saldo=0):
        super().__init__(agencia, numero, saldo)

    def sacar(self, banco, cliente, valor):
        if banco.agencia != self.agencia:
            return print(f'Essa conta não pertence ao banco {banco.nome}')

        for conta in banco.contas.values():
            if self == conta['conta'] and cliente == conta['cliente']:
                if valor > self.saldo:
                    return print(f'Você pode sacar até: R${self.saldo:.2f}.')

                self._saldo -= valor

        return print('Esse cliente não pertence a esse banco.')
