import os
import time
from empresa import *
from individuo import *

#inicio
print('======================================')
print('  Calculadora de credito de carbono ')
print('======================================')
print('Aviso: Todos os dados contidos nesse programa por parte do GHG protocol')

#funcao limpa tela
def limpatela():
    # Verifica sistema operacional
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # linux ou Mac1
        os.system('clear')

#menu
while True:
    print(' [1] - Empresa \n [2] - Individuo \n [0] - Sair')
    opcao = str(input('Selecione uma opção: '))
    if opcao == '1':
        empresa()#chama função empresa
        print('Finalizando o programa....')
        time.sleep(1)
        break
    elif opcao == '2':
        individuo()#chama função individuo
        print('Finalizando o programa....')
        time.sleep(1)
        break
    elif opcao == '0':
        print('Saindo do programa....')
        time.sleep(2)
        break
    else:
        print('Erro: Selecione uma opção valida.')
        limpatela()

