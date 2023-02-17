from aula79.classes.contapoupanca import ContaPoupanca
from aula79.classes.contacorrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)


cp.depositar(20)
cp.sacar(10)

cc = ContaCorrente(1111, 3333, 0, 500)

cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)