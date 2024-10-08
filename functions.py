import os

def limpa_tela():
    os.system('cls')

def empresa():
    #Selecionar o tipo de empresa
    while True:
        print(' [1] - Serviços \n [2] - Industria \n [3] - Comercio \n [4] - outros')
        tpEmpresa = str(input('Ramo da empresa: '))
        if tpEmpresa == '1':
            print('Tipo selecionado: [1] - Serviços')
            break
        elif tpEmpresa == '2':
            print('Tipo selecionado: [2] - Industria')
            break
        elif tpEmpresa == '3':
            print('Tipo selecionado: [3] - Comercio')
            break
        elif tpEmpresa == '4':
            print('Tipo selecionado: [4] - Outros')
            break
        else:
            print('Erro: Selecione uma opção valida.')
    
    #cadastro da empresa
    print('Agora será necessario informar alguns dados da empresa')
    cadEmpresa = []
    cadEmpresa.append(str(input('Nome da empresa: ')))
    cadEmpresa.append(str(input('Nome do Responsavel: ')))
    cadEmpresa.append(str(input('Telefone da empresa: ')))
    cadEmpresa.append(str(input('Ano de inventario: ')))

def individuo():
    #cadastro do individuo
    print('Agora será necessario informar alguns dados seus')
    cadIndividuo = []
    cadIndividuo.append(str(input('Nome: ')))
    cadIndividuo.append(str(input('Idade: ')))
    cadIndividuo.append(str(input('Telefone: ')))
    cadIndividuo.append(str(input('Ano inventario: ')))

    #Cadastro de veiculos
    while True:
        print('Você possue algum veiculo automotor? ')
        print('[1] - Sim | [0] - Não')
        veiculo = str(input())
        if veiculo == '1':
            qtVeiculo = int(input('Quantos veiculos automotores você possue? '))
            list_mdVeiculo = []
            list_kmVeiculo = []
            list_combVeiculo = []
            for i in range(qtVeiculo):
                list_mdVeiculo.append(str(input(f'Digite o modelo do {i+1}º veiculo: ')))
                list_kmVeiculo.append(str(input(f'Digite a media de Km mensal do {i+1}º veiculo: ')))
                tpComb = str(input(' ==================== \n Tipo de combustivel \n ==================== \n [1] - Gasolina \n [2] - Etanol \n [3] - Diesel \n [4] - Biodiesel \n [5] - Eletrico'))
                while True:
                    if tpComb == '1' and '2' and '3' and '4':
                        list_combVeiculo.append(str(input(f'Digite o consumo médio em L do {i+1}º veiculo: ')))
                        break
                    elif tpComb == '5':
                        list_combVeiculo.append(str(input(f'Digite o consumo médio em kw/h do {i+1}º veiculo: ')))
                        break
                    else:
                        print('Erro: Digite um tipo de combustivel valido.')            
        elif veiculo == '0':
            break
        else:
            print('Erro: selecione uma opção valida.')
    
    #Tipo de enrgia
    consEnergia = float(input('Digite a media mensal de consumo de enrgia em Kw/h de sua residência: '))

    print(list_mdVeiculo)
    print(list_kmVeiculo)
    print(list_combVeiculo)
