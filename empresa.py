def empresa():
    print("Antes de começarmos será necessario cadastrar a empresa")
    dadosEmpresa = []
    dadosEmpresa.append(str(input('Nome da organização: ')))
    dadosEmpresa.append(str(input('Endereço da organização: ')))
    dadosEmpresa.append(str(input('Nome do responsavel: ')))
    dadosEmpresa.append(str(input('Telefone do Responsavel: ')))
    while True:
        anoInventariado = int(input('Ano Inventariado: '))
        if 2006 <= anoInventariado <= 2023:
            dadosEmpresa.append(anoInventariado)
            break
        else:
            print('Erro: Ano selecionado e invalido. \n o Ano tem que ser de 2006 até 2023')

#tipos de combustivel
    etanol = [] #1.58kg CO2/litro
    gasolina = [] #2.24kg CO2/litro
    diesel = [] #2.63kg CO2/litro
    biodiesel = [] #2.46kg CO2/litro
    glp = [] #2.93 CO2/tonelada
#Escopo1
#Combustão estacionaria
    print('Combustão estacionária \n A combustão estacionária é a queima de combustíveis em equipamentos estacionários, como fontes de aquecimento e combustíveis padrão')
    print('A empresa faz uso de combustível estacionário? \n [1] - Sim | [0] - Não')
    combEstacionaria = str(input())
    while True:
        if combEstacionaria == '1':
            while True:
                print(' Selecione um tipo de combustivel: \n [1] - Etanol \n [2] - Gasolina \n [3] - Diesel \n [4] - BioDiesel \n [5] - glp \n [0] - Sair')
                slComb = str(input())
                if slComb == '1':  
                    etanol.append(float(input('Qual e o consumo médio em litros de Etanol por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combEstacionaria = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '2':
                    gasolina.append(float(input('Qual e o consumo médio em litros de Gasolina por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combEstacionaria = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '3':
                    diesel.append(float(input('Qual e o consumo médio em litros de Diesel por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combEstacionaria = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '4':
                    biodiesel.append(float(input('Qual e o consumo médio em litros de BioDiesel por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combEstacionaria = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '5':
                    glp.append(float(input('Qual e o consumo médio em litros de GLP (Gás liquefeito de Petrólio) por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combEstacionaria = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '0':
                    combEstacionaria = '0'
                    break
                else:
                    print('Erro: Digite um tipo de combustivel valido.')
        elif combEstacionaria == '0':
            break        
        else:
            print('Erro: Digite uma opção valida')
#combustão movel
    print(' Combustão Movel \n Combustão móvel se refere às emissões de gases de efeito estufa provenientes de veículos que queimam combustíveis fósseis como gasolina, diesel, gás natural, etanol e outros.')
    print('A empresa faz uso de combustível estacionário? \n [1] - Sim | [0] - Não')
    combMovel = str(input())
    while True:
        if combMovel == '1':
            while True:
                print(' Selecione um tipo de combustivel: \n [1] - Etanol \n [2] - Gasolina \n [3] - Diesel \n [4] - BioDiesel \n [5] - glp \n [0] - Sair')
                slComb = str(input())
                if slComb == '1':  
                    etanol.append(float(input('Qual e o consumo médio em litros de Etanol por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combMovel = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '2':
                    gasolina.append(float(input('Qual e o consumo médio em litros de Gasolina por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combMovel = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '3':
                    diesel.append(float(input('Qual e o consumo médio em litros de Diesel por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combMovel = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '4':
                    biodiesel.append(float(input('Qual e o consumo médio em litros de BioDiesel por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combMovel = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '5':
                    glp.append(float(input('Qual e o consumo médio em litros de GLP (Gás liquefeito de Petrólio) por mês? ')))
                    print('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não')
                    slEscolha = str(input())
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combMovel = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '0':
                    combMovel = '0'
                    break
                else:
                    print('Erro: Digite um tipo de combustivel valido.')
        elif combMovel == '0':
            break        
        else:
            print('Erro: Digite uma opção valida')
#Calculo combustivel
    etanol = (12 * sum(etanol))
    gasolina = (12 * sum(gasolina))
    diesel = (12 * sum(diesel))
    biodiesel = (12 * sum(biodiesel))
    glp = (12 * sum(glp))
    etanol = ((etanol * 1.58)/1000) #1.58kg CO2/litro
    gasolina = ((gasolina * 2.24)/1000) #2.24kg CO2/litro
    diesel = ((diesel * 2.63)/1000) #2.63kg CO2/litro
    biodiesel = ((biodiesel * 2.46)/1000) #2.46kg CO2/litro
    glp = ((glp * 2.93)) #2.93 CO2/tonelada
    print(f'Toneladas: {etanol}')
    print(f'Toneladas: {gasolina}')
    print(f'Toneladas: {diesel}')
    print(f'Toneladas: {biodiesel}')
    print(f'Toneladas: {glp}')

