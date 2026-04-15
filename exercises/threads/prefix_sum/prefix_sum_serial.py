import time
import numpy as np

LIST_SIZE = 1000000

def main():
    listaA = np.random.randint(1, 101, size=LIST_SIZE)
    listaB = [0] * LIST_SIZE

    start=time.time()

    listaB[0] = listaA[0]

    for i in range(1, len(listaA)):
        listaB[i] = listaB[i-1] + listaA[i]
    # fim for

    end=time.time()

    print( f'Demorou {end - start} segundos')
# fim def

if __name__ == "__main__":
    main()
# fim if
