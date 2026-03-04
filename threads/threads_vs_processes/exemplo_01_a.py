# Bloco 1
#importando bibliotecas necessárias
import time
import random as rd
import numpy as np
from threading import Thread

# Bloco 2
# Múltiplas  Threads.
def do_something(sec):
  print('Doing Something...')
  time.sleep(sec)
  print('Done!')

threads=[]
start=time.time()

for _ in range(1000):
   new_thread = Thread(target=do_something, args=[1])
   threads.append(new_thread)
   new_thread.start()

for t in threads:
  t.join()



end=time.time()

print( f'Tempo decorrido:{end-start}')

