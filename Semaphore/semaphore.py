import threading
import time

semaphore = threading.Semaphore(1)  # Apenas uma thread por vez

def secao_critica(thread_id):
    semaphore.acquire()  # Adquire o semáforo
    try:
        print(f"Thread {thread_id} está na região crítica.")
        time.sleep(1)
        print(f"Thread {thread_id} saiu da região crítica.")
    finally:
        semaphore.release()  # Libera o semáforo

def process(thread_id):
    for _ in range(3):
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
