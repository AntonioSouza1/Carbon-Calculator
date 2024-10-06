import time
import os
nome = str(input('Olá, qual é o seu nome? '))
def limpar_tela():
    os.system('cls') #limpar a tela
limpar_tela()
print('________________________________________________________________________')
print('                                                  ')
print(f'   Bem Vindo Sr. {nome}, a Calculadora de credito de carbono   ')
print('________________________________________________________________________')
print('Carregando...')
time.sleep(2)#Pausa simulada para carregamento

def cadEmpresa():
    print('Cadastro da empresa')
    cadastro_empresa = []
    cadastro_empresa.append(str(input('Digite o nome: ')))
    cadastro_empresa.append(str(input('Digite o CNPJ: ')))
    cadastro_empresa.append(str(input('Digite o nome do responsavel: ')))


def individuo():
    print('Cadastro da Pessoal')
    cadastro_empresa = []
    cadastro_empresa.append(str(input('Digite o nome: ')))
    cadastro_empresa.append(str(input('Digite o cpf: ')))
    cadastro_empresa.append(str(input('Digite o Idade: ')))

while True:
    print('Selecione o responsavel por essas emissões')
    tipo = str(input('Digite: [0] - empresa [1] - Individuo '))
    if tipo == '0':
        cadEmpresa()
        break
    elif tipo == '1':
        individuo()
        break
    else:
        print('Erro: Selecione uma opção válida.')
        time.sleep(1)
        limpar_tela()