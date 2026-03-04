#importando bibliotecas necessárias
import time
from threading import Thread
# Agora sim com múltiplas  Threads.
def do_something(sec):
  print('Doing Something...')
  time.sleep(sec)
  print('Done!')

threads=[]
start=time.time()

for _ in range(5):
   new_thread = Thread(target=do_something, args=[1])
   threads.append(new_thread)
   new_thread.start()

for t in threads:
  t.join()



end=time.time()

print( f'Tempo decorrido:{end-start}')

