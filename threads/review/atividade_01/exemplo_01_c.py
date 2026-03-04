#importando bibliotecas necessárias
import time
from threading import Thread
# Agora sim com múltiplas  Threads.
def task(sec):
  print('Doing Something...')
  time.sleep(sec)
  print('Done!')


start=time.time()

for _ in range(5):
   new_thread = Thread(target=task, args=[1])
   new_thread.start()


end=time.time()

print( f'Tempo decorrido:{end-start}')

