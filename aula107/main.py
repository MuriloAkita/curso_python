from time import sleep
from threading import Thread
from threading import Lock

"""class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        
        super().__init__()
        
    def run(self):
        sleep(self.tempo)
        print(self.texto)
        
        
t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)"""
    
    
"""def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)
    
t = Thread(target=vai_demorar, args=('Olá Mundo', 5))
t.start()

while t.is_alive():
    print('Esperando a thread.')
    sleep(2)"""
    

class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()
    
    def comprar(self, quantidade):
        self.lock.acquire()
        
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()
            return
        
        sleep(1)
        
        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s).' 
              f'Ainda temos {self.estoque} em estoque')
        self.lock.release()
        
if __name__ == '__main__':
    ingressos = Ingresso(10)
    
    threads = []
    for i in range(20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)
        
    for t in threads:
        t.start()
            
    executando = True
    while executando:
        executando = False
        
        for t in threads:
            if t.is_alive():
                executando = True
                break
                
    print(ingressos.estoque)
    