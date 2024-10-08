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

#Moradia
    qtMoradores = int(input('Digite a quantidade de moradores: '))
    consAgua = float(input('Digite o consumo médio de água em m³/mês: '))
    residuos = float(input('Digite a quantidade de residuos em Kg/dia: '))
    consEnergia = float(input('Digite o consumo de energia eletrica em reais: '))
    consGas = float(input('Digite o consumo de gás em reais: '))
    
#transporte
    #Veiculo proprio
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
    #Transporte publico
    #ônibusUrbano
    while True:
        print('Você faz uso de ônibus urbano? ')
        print('[1] - Sim | [0] - Não')
        onibusUrbano = str(input())
        if onibusUrbano == '1':
            onibusUrbano_dia = int(input('quantas dias por mês você faz o uso desse meio de transporte? '))
            onibusUrbano_km = int(input('Quantos km por dia você anda com esse meio de transporte? '))
            break
        elif onibusUrbano == '0':
            break
        else:
            print('Erro: Digite uma opção valida.')
    #ônibusViagem
    while True:
        print('Você faz uso de ônibus de viagem? ')
        print('[1] - Sim | [0] - Não')
        onibusViagem = str(input())
        if onibusViagem == '1':
            onibusViagem_dia = int(input('quantas dias por mês você faz o uso desse meio de transporte? '))
            onibusViagem_km = int(input('Quantos km por dia você anda com esse meio de transporte? '))
            break
        elif onibusViagem == '0':
            break
        else:
            print('Erro: Digite uma opção valida.')
    #trem
    while True:
        print('Você faz uso de Trem? ')
        print('[1] - Sim | [0] - Não')
        trem = str(input())
        if trem == '1':
            trem_dia = int(input('quantas dias por mês você faz o uso desse meio de transporte? '))
            trem_km = int(input('Quantos km por dia você anda com esse meio de transporte? '))
            break
        elif trem == '0':
            break
        else:
            print('Erro: Digite uma opção valida.')
    #metro
    while True:
        print('Você faz uso de Trem? ')
        print('[1] - Sim | [0] - Não')
        metro = str(input())
        if metro == '1':
            metro_dia = int(input('quantas dias por mês você faz o uso desse meio de transporte? '))
            metro_km = int(input('Quantos km por dia você anda com esse meio de transporte? '))
            break
        elif metro == '0':
            break
        else:
            print('Erro: Digite uma opção valida.')
    
    #viagens
    while True:
        print('Você você viaja de avião? ')
        print('[1] - Sim | [0] - Não')
        aviao = str(input())
        if aviao == '1':
            viagemAviao = int(input('Quantas viagem você consuta fazer por ano?'))
            while True:
                print('[1] - Curta (até 700km) \n [2] - Média (2.000km) \n [3] - Longa (mais de 7.000km)')
                distAviao = str(input())
                if distAviao == '1':
                    break
                elif distAviao == '2':
                    break
                elif distAviao == '3':
                    break
                else:
                    print('Erro: digite uma opção valida.' )           
            break
        elif aviao == '0':
            break
        else:
            print('Erro: Digite uma opção valida. ')
    
