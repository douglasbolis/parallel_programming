# Bloco 1
# Criando o Vetor
import numpy as np
lista= np.random.randint(0, high=5000000,size=5000000)

# Bloco 2
import time
import threading
lock=threading.Lock()
threads = []
result = 0
n_threads = 4

bloco = len(lista) // n_threads

def task(lst,idx, inic, fin):
    print('{0} - Somando minha parte: de {1} a {2}'.format(idx, inic, fin))
    # usando uma variável global para acumular o resultado final
    minhasoma=0
    global result

    for i in lst[inic:fin]:
        minhasoma+=i
    print('{0} - Done! Minha soma: {1}'.format(idx, minhasoma))
    with lock:  # Usando 'with' para gerenciar o lock
        result += minhasoma

start = time.time()

for x in range(n_threads):
    inicio = x * bloco
    final = inicio + bloco if x < n_threads - 1 else len(lista)  # Último bloco pode ser maior
    new_thread = threading.Thread(target=task, args=(lista,x, inicio, final))
    threads.append(new_thread)
    new_thread.start()

for t in threads:
    t.join()

print("O resultado final é: {0}".format(result))
end = time.time()

print(f'Tempo decorrido: {end - start:.4f} segundos')

