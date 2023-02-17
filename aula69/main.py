from pessoa import Pessoa

p1 = Pessoa('Murilo', 21)
p2 = Pessoa('Luiz', 32)

p1.comer('maçã')
p2.comer('banana')
p1.parar_comer()
p2.parar_comer()
p1.parar_comer()
p1.comer('maçã')
p1.parar_comer()
p1.falar('jogos')
p2.falar('POO')
p1.parar_falar()
p1.parar_falar()
p1.falar('jogos')

print(p1.get_ano_nascimento())
