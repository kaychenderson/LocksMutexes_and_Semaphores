<h1 align="center" style="font-weight: bold;">🚦 Semáforos 🚦</h1> 
<p align="center"> 
    <a href="#code">Descrição do Código</a> • 
    <a href="#output">Saída do Código</a>
</p>

### PEX0093 - Sistemas Operacionais
##### Professor: [Reudismam Rolim](https://github.com/reudismam)

##### Discrentes: Amanda Gonçalves, Amanda Santiago, Joana Larissa e Kayc Henderson

#### Bacharelado Interdisciplinar em Tecnologia da Informação - UFERSA

<h2 id="code" style="font-weight: bold; font-size: 2rem">Descrição do Código</h2>

Este código demonstra o uso de `threading.Lock()` em Python para garantir exclusão mútua em uma região crítica, onde apenas uma thread pode acessar determinado bloco de código por vez.

## Explicação Linha a Linha:
```bash
import threading
import time
```
Importamos os módulos necessários:

`threading`: permite o uso de threads e mecanismos de sincronização. <br>
`time`: utilizado para simular atrasos com `sleep`.

```bash
semaphore = threading.Semaphore(5)  # Apenas uma thread por vez
```
Criamos um semáforo que permite até 5 threads simultaneamente na região crítica.

```bash
def secao_critica(thread_id):
    semaphore.acquire()  # Adquire o semáforo
    try:
        print(f"Thread {thread_id} está na região crítica.")
        time.sleep(1)
        print(f"Thread {thread_id} saiu da região crítica.")
    finally:
        semaphore.release()  # Libera o semáforo
```
A função `secao_critica`(thread_id) define a região crítica:
- `semaphore.acquire()`: adquire uma "vaga" no semáforo, bloqueando se não houver vagas disponíveis.
- O bloco `try-finally` garante que o semáforo seja liberado mesmo em caso de erro.
- `time.sleep(1)`: simula uma tarefa demorada na região crítica.
- As mensagens indicam a entrada e saída da região crítica.

```bash
def process(thread_id):
    for _ in range(3):
        print(f"Thread {thread_id} está na região NÃO crítica.")
        time.sleep(1)
        critical_section(thread_id)
```
A função process(thread_id) executa três iterações:

- Imprime uma mensagem indicando que a thread está na região não crítica.
- Aguarda 1 segundo para simular uma operação externa.
- Chama `secao_critica(thread_id)` para acessar a região protegida.

```bash
threads = []
```
Inicializa uma lista vazia para armazenar as threads.

```bash
for i in range(2):
    t = threading.Thread(target=process, args=(i,))
    threads.append(t)
    t.start()
```
Cria duas threads que executam a função process. Para cada thread:

- `threading.Thread(target=process, args=(i,))`: cria uma thread associada ao processo.
- `t.start()`: inicia a execução da thread.

```bash
for t in threads:
    t.join()
```
Aguarda a conclusão de todas as threads antes de encerrar o programa.

<h2 id="output" style="font-weight: bold; font-size: 2rem">Saída do Código</h2>
Exemplo de saída do código:

```bash
Thread 0 está na região NÃO crítica.
Thread 1 está na região NÃO crítica.
Thread 0 está na região crítica.
Thread 1 está na região crítica.
Thread 0 saiu da região crítica.
Thread 0 está na região NÃO crítica.
Thread 1 saiu da região crítica.
Thread 1 está na região NÃO crítica.
```
- As mensagens "região NÃO crítica" são exibidas independentemente da ordem.
- Até 5 threads poderiam acessar a "região crítica" ao mesmo tempo, mas neste exemplo apenas duas threads estão presentes.
- As chamadas a time.sleep() podem causar variações na ordem exata das mensagens.