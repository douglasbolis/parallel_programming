#1. Definindo  o código a ser executado neste código, sincronamente.
#importando bibliotecas necessáriass
import time
from threading import Thread

def task(sec):
  print('Starting Task:')
  time.sleep(sec)
  print('Done')

# Medindo o Tempo de Execução
start=time.time()

task(3)

end=time.time()

print( f'Tempo decorrido:{end-start}')


