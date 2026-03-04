# Bloco 1
# Criando o Vetor
import numpy as np
lista= np.random.randint(0, high=5000000,size=5000000)

# Bloco 2
import time
import threading
import numpy as np

threads = []
n_threads = 4
result = np.zeros(n_threads)
bloco = len(lista) // n_threads

def task(lst,idx, inic, fin):
    print('{0} - Somando minha parte: de {1} a {2}'.format(idx, inic, fin))
    # usando uma variável global para acumular o resultado final
    minhasoma=0
    global result

    for i in lst[inic:fin]:
        minhasoma+=i
    print('{0} - Done! Minha soma: {1}'.format(idx, minhasoma))
    result[idx]= minhasoma

start = time.time()

for x in range(n_threads+1):
    inicio = x * bloco
    final = inicio + bloco -1 if x < n_threads else len(lista)  # Último bloco pode ser maior
    new_thread = threading.Thread(target=task, args=(lista,x, inicio, final))
    threads.append(new_thread)
    new_thread.start()

for t in threads:
    t.join()

print("O resultado final é: {0}".format(np.sum(result)))
end = time.time()

print(f'Tempo decorrido: {end - start:.4f} segundos')

# Bloco 3
# Elabore um programa paralelo em nivel de thread que calcule a soma dos quadrados dos elementos do vetor **vet** compara a versao serial com a paralela com 4 threads


import numpy as np
import time

np.random.seed(42)
vet = np.random.randint(0, high=1000000, size=1000000)
soma = 0

start = time.time()
for i in range(len(vet)):
  soma += vet[0]**2

end = time.time()
print(soma)
print("tempo decorido: " + str(end-start) + " segundos")

# Bloco 4
import numpy as np
import time
import threading

threads = []
n_threads = 4
result = 0
indice = 0

np.random.seed(42)
vet = np.random.randint(0, high=1000000, size=1000000)

start = time.time()

def task():
  global result
  global indice
  global vet
  with threading.Lock():
    while indice < len(vet):
        result += vet[indice]**2
        indice += 1

for i in range(n_threads):
  new_thread = threading.Thread(target=task)
  threads.append(new_thread)
  new_thread.start()

for t in threads:
    t.join()

end = time.time()
print(result)
print("tempo decorido: " + str(end-start) + " segundos")


