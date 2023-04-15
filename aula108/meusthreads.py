from time import sleep
from threading import Thread, Lock

# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo
        
#         super().__init__()
        
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)
            
# t1 = MeuThread('Thread 1', 5)
# t1.start()

# for i in range(20):
#     print(i)
#     sleep(1)

# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)
    
    
# t = Thread(target=vai_demorar, args=('Hello World! 1', 2))
# t.start()

# t2 = Thread(target=vai_demorar, args=('Hello World! 2', 1))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('Hello World 3!', 3))
# t3.start()

# for i in range(10):
#     print(i)
#     sleep(.5)
        
# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)
    
# t = Thread(target=vai_demorar, args=('Hello World! 1', 10))
# t.start()

# while t.is_alive():
#     print('Waiting thread...')
#     sleep(5)

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()
        
    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Insufficient tickets.')
            self.lock.release()
            return
        
        sleep(1)
        
        self.estoque -= quantidade
        print(f'You bought {quantidade} ticket(s). '
              f'We have {self.estoque} tickets for sale')
        
        self.lock.release()
        
if __name__ == '__main__':
    ingressos = Ingressos(50)
    
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
        
    print(ingressos.estoque)
        