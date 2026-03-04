# Bloco 1
# Criando o Vetor
import numpy as np
lista= np.random.randint(0, high=5000000,size=5000000)

# Bloco 2
import time
from threading import Thread,Lock
start=time.time()
meu_arr_ordenado = np.sort(lista) # cria um arranjo ordenado em ordem decrescente

end=time.time()
print(meu_arr_ordenado)
print( f'Tempo decorrido:{end-start}')

# Bloco 3
def quicksort_thread(start_idx, end_idx, arr, result, idx):
    part = arr[start_idx:end_idx]
    result[idx] = np.sort(part)  # Usando np.sort() que é quicksort por padrão

# Função para mesclar dois vetores ordenados
def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    print
    return result

# Função para mesclar múltiplos vetores ordenados
def multi_merge(parts):
    while len(parts) > 1:
        merged_parts = []
        for i in range(0, len(parts), 2):
            if i + 1 < len(parts):
                merged_parts.append(merge(parts[i], parts[i+1]))
            else:
                merged_parts.append(parts[i])
        parts = merged_parts
    return parts[0]

# Iniciando o cronômetro
start = time.time()

# Definindo o número de threads
num_threads = 4
part_size = len(lista) // num_threads

# Lista para armazenar os resultados das threads
result = [None] * num_threads

# Criando as threads
threads = []
for i in range(num_threads):
    start_idx = i * part_size
    # Garantir que a última parte pegue até o final do vetor
    end_idx = (i + 1) * part_size if i != num_threads - 1 else len(lista)
    thread = Thread(target=quicksort_thread, args=(start_idx, end_idx, lista, result, i))
    threads.append(thread)
    thread.start()

# Esperando as threads terminarem
for thread in threads:
    thread.join()

# Mesclando as partes ordenadas
final_result = multi_merge(result)
# Finalizando o cronômetro
end = time.time()

# Exibindo o vetor ordenado e o tempo de execução
# print(final_result)  # Aqui imprimimos o vetor final ordenado
print(f'Tempo decorrido com Quicksort paralelo: {end - start}')

# Bloco 4
import time
from threading import Thread,Lock

result=0
start=time.time()
for i in lista:
  result+=i

print("O resultado final  é:{}".format(result))
end=time.time()

print( f'Tempo decorrido:{end-start}')

