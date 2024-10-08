from functions import *
import time
print('====================================')
print(' Calculadora de credito de carbono')
print('====================================')
while True:
    print('[0] - Empresa | [1] - Individuo')
    finalidade = str(input('Selecione uma finalizade: '))
    if finalidade == '0':
        empresa()
        break
    elif finalidade == '1':
        individuo()
        break
    else:
        print('Erro: Selecione uma opção valida. ')
    

