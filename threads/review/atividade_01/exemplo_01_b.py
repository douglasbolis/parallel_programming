#importando bibliotecas necessárias
import time
from threading import Thread
def task(sec):
  print('Starting Task...')
  time.sleep(sec)
  print('Done!')


start=time.time()

for _ in range(5):
   task(1)

end=time.time()

print( f'Tempo decorrido:{end-start}')

