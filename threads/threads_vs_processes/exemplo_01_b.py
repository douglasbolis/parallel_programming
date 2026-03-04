# Bloco 1
#importando bibliotecas necessárias
import time
import random as rd
import numpy as np
from threading import Thread
from multiprocessing import Process

# Bloco 2
#  Multi-processosa custom function that blocks for a moment
def task(sleep_time, message):
    # block for a moment
    time.sleep(sleep_time)
    # display a message
    print(message)

# entry point
if __name__ == '__main__':
    # create a process
    process = Process(target=task, args=(1.5, 'New message from another process'))
    # run the process
    process.start()
    # wait for the process to finish
    print('Waiting for the process...')
    process.join()


