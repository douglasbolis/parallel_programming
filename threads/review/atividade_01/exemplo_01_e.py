
# Agora sim com múltiplas  Threads.
#importando bibliotecas necessárias
import time
from threading import Thread
def do_something(sec):
  time.sleep(sec)
  return 'Done!'


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

