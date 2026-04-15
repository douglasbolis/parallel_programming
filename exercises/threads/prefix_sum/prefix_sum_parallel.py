import time
import numpy as np
from threading import Thread

def prefix_sum(sec):
    time.sleep(sec)
    return 'Done!'
# fim def

def main():
    lista = np.random.randint(1, 101, size=1000000)
    threads=[]
    start=time.time()

    for _ in range(1000):
        new_thread = Thread(target=prefix_sum, args=[1])
        threads.append(new_thread)
        new_thread.start()
    # fim for

    for t in threads:
        t.join()
    # fim for

    end=time.time()

    print( f'Tempo decorrido:{end-start}')
# fim def

if __name__ == "__main__":
    main()
# fim if
