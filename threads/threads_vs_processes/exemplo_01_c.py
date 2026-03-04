# Bloco 1
#importando bibliotecas necessárias
import time
import random as rd
import numpy as np
# SuperFastPython.com
# example of extending the Process class

from multiprocessing import Process

# Bloco 2
import time
from multiprocessing import Pool
def square(x):
   return x * x
if __name__ == '__main__':
   start=time.time()
   with Pool(4) as pool:
       results = pool.map(square, [1, 2, 3, 4, 5,7])
       end=time.time()


       print("tempo: ",end-start)
       print ("resultado: ", results)


