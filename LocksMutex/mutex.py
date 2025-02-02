import threading
import time

mutex = threading.Lock()  # Inicializa o mutex

def secao_critica(thread_id):
    with mutex:  # Adquire o mutex automaticamente e libera ao sair
        print(f"Thread {thread_id} está na região crítica.")
        time.sleep(1)
        print(f"Thread {thread_id} saiu da região crítica.")

def process(thread_id):
    for _ in range(3):  # Simula múltiplas execuções
        print(f"Thread {thread_id} está na região NÃO crítica.")
        time.sleep(1)
        secao_critica(thread_id)

threads = []

for i in range(2):
    t = threading.Thread(target=process, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()