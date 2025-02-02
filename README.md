<h1 align="center" style="font-weight: bold;">🔒 Locks Mutex e Semáforos 🚦</h1> 
<p align="center"> 
    <a href="#about">Sobre os Algoritmos</a> • 
    <a href="#features">Funcionalidades</a> • 
    <a href="#install">Instalação</a> • 
    <a href="#usage">Como Usar</a> 
</p>

### PEX0093 - Sistemas Operacionais
##### Professor: [Reudismam Rolim](https://github.com/reudismam)

##### Discrentes: Amanda Gonçalves, Amanda Santiago, Joana Larissa e Kayc Henderson

#### Bacharelado Interdisciplinar em Tecnologia da Informação - UFERSA

<h2 id="tech" style="font-weight: bold; font-size: 2rem">Tecnologia Utilizada</h2> 
<img align="center" alt="python" src="https://img.shields.io/badge/Python-FFFFFF?style=for-the-badge&logo=python&logoColor=black"/>

<h2 id="about" style="font-weight: bold; font-size: 2rem">Sobre o Algoritmo</h2>
Este projeto implementa duas abordagens clássicas para a exclusão mútua em sistemas concorrentes:

- Locks Mutex: Um mecanismo simples que garante acesso exclusivo à região crítica de um processo/thread por vez.
- Semáforos: Um conceito mais genérico que controla o acesso simultâneo a recursos compartilhados, podendo permitir múltiplas permissões simultâneas dependendo do valor do semáforo. <br>

Ambas as implementações buscam resolver problemas comuns em ambientes multithreaded, como condições de corrida e sincronização inadequada.

<h2 id="features" style="font-weight: bold; font-size: 2rem">⚙ Funcionalidades</h2> 
<h3> 🔐 Locks Mutex: </h3> 
- Exclusão mútua garantida para apenas um processo por vez na região crítica. <br> 
- Evita condições de corrida em recursos compartilhados. 
<h3> 🚦 Semáforos: </h3> 
- Controle flexível de acesso a recursos. <br>
- Suporte a múltiplos processos simultâneos dependendo do valor inicial do semáforo (`N > 1`).  <br>
- Sincronização eficiente em cenários concorrentes. <br><br>

| Aspecto              | Locks Mutex  | Semaphore  |
|-----------------------|-------------|------------|
| **Valor**             | 0 ou 1      | Inteiro (N)|
| **Exclusão Mútua**    | Sim         | Opcional   |
| **Número de Threads** | 1           | Até N      |
| **Controle**          | Thread que bloqueia deve liberar | Qualquer thread pode liberar |
| **Complexidade**      | Simples     | Mais flexível |

<div align="center">
    <img src="https://github.com/user-attachments/assets/8add690c-20fa-4f2b-a4af-6a3c3a54d1ed" height="180px" width="300px">
    <img src="https://github.com/user-attachments/assets/12467252-730c-47d4-991e-11c7053d0fbb" width="300px">
    <h3>Locks Mutex | Semaphore</h3>
</div>

<h2 id="install" style="font-weight: bold; font-size: 2rem">📦 Instalação</h2>
Para rodar o código em sua máquina, siga os passos abaixo:

#### 1. Clone este repositório:
```bash
git clone https://github.com/kaychenderson/LocksMutexes_and_Semaphores.git  
```

#### 2. Acesse o diretório do projeto:
```bash
cd LocksMutex
cd Semaphore
```

#### 1. Compile e execute os arquivos do código:
```bash
python mutex.py
python semaphore.py 
```

<h2 id="usage" style="font-weight: bold; font-size: 2rem">💡 Como Usar</h2>
Após executar o código, você verá mensagens no console indicando o comportamento sincronizado das threads.

- Para Locks Mutex, apenas uma thread acessará a região crítica por vez.

- Para Semáforos, dependendo do valor inicial (N), múltiplas threads podem acessar simultaneamente, respeitando o controle definido pelo semáforo.
