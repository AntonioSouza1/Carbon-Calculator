from pickle import PROTO


def empresa():
    print("Antes de começarmos será necessário cadastrar a empresa")
    dadosEmpresa = {}
    dadosEmpresa['nome'] = (input('Nome da organização: '))
    dadosEmpresa['endereco'] = (input('Endereço da organização: '))
    dadosEmpresa['nomeResponsavel'] = (input('Nome do responsável: '))
    dadosEmpresa['telefoneResponsavel'] = (input('Telefone do Responsável: '))
    while True:
        anoInventariado = int(input('Ano Inventariado: '))
        if 2006 <= anoInventariado <= 2023:
            dadosEmpresa['anoInventario'] = (anoInventariado)
            break
        else:
            print('Erro: O Ano selecionado e invalido. \nO Ano tem que ser de 2006 até 2023')
    print('****** Ramo da empresa ****** \n [1] - Agro \n [2] - Industrial \n [3] - Outros')
    rmEmpresa = input('Selecione o ramo da empresa: ')
    while True:
        if rmEmpresa == '1':
            print('Ramo selecionado: Agro')
            break
        elif rmEmpresa == '2':
            print('Ramo selecionado: Industria')
            break
        elif rmEmpresa == '3':
            print('Ramo selecionado: Outros')
            break
        else:
            print('Erro: Selecione um ramo valido. ')
#dados Fator de conversão
    comb = {
        'etanol': 1.58, #CO2/litro
        'gasolina': 2.24, #CO2/litro
        'diesel': 2.63, #CO2/litro
        'biodiesel': 2.46, #CO2/litro
        'glp': 2.93 #CO2/litro
    }
    arCond = {
        'arPequeno': 0.5, #kg por hora
        'arMedio': 1.5, #kg por hora
        'arGrande': 3, #kg por hora
        'arIndustrial': 4 #kg por hora
    }
    prodIndustrial = {
        'ProdAco' : 1.8, #kg de co2 por kg produzido
        'ProdCimento' : 0.9, #kg de co2 por kg produzido
        'ProdPapel' : 0.5, #kg de co2 por kg produzido
        'ProdVidro' : 0.6, #kg de co2 por kg produzido
        'ProdAluminio' : 12, #kg de co2 por kg produzido
        'ProdAmonia' : 1.8, #kg de co2 por kg produzido
        'ProdEtanol' : 1.6, #kg de co2 por kg produzido
        'ProdEletricidade_Carvao' : 0.9, #kg de co2 por kg produzido
        'ProdEletricidade_GasNat' : 0.4, #kg de co2 por kg produzido
        'ProdEletricidade_Petróleo' : 0.7 #kg de co2 por kg produzido
    }
#Entrada de combustível

    etanol = []
    gasolina = []
    diesel = []
    biodiesel = []
    glp = []

#Combustão estacionaria
    print('Combustão estacionária \n A combustão estacionária é a queima de combustíveis em equipamentos estacionários, como fontes de aquecimento e combustíveis padrão')
    combEstacionaria = input('A empresa faz uso de combustível estacionário? \n[1] - Sim | [0] - Não \n')
    while True:
        if combEstacionaria == '1':
            while True:
                print('****** combustíveis ****** \n [1] - Etanol \n [2] - Gasolina \n [3] - Diesel \n [4] - BioDiesel \n [5] - glp \n [0] - Sair \n')
                slComb = input('Selecione o tipo de combustivel: ')
                if slComb == '1':
                    etanol.append(float(input('Qual e o consumo médio em litros de Etanol por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
                    if slEscolha == '1':
                        print('Aguarde...')
                    elif slEscolha == '0':
                        combEstacionaria = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '2':
                    gasolina.append(float(input('Qual e o consumo médio em litros de Gasolina por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
                    if slEscolha == '1':
                        print('Aguarde...')
                    elif slEscolha == '0':
                        combEstacionaria = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '3':
                    diesel.append(float(input('Qual e o consumo médio em litros de Diesel por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
                    if slEscolha == '1':
                        print('Aguarde...')
                    elif slEscolha == '0':
                        combEstacionaria = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '4':
                    biodiesel.append(float(input('Qual e o consumo médio em litros de BioDiesel por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combEstacionaria = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '5':
                    glp.append(float(input('Qual e o consumo médio em litros de GLP (Gás liquefeito de Petrólio) por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
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
                    print('Erro: Digite um tipo de combustível valido.')
        elif combEstacionaria == '0':
            break        
        else:
            print('Erro: Digite uma opção valida')

#combustão movel
    print('Combustão Movel \nCombustão móvel se refere às emissões de gases de efeito estufa provenientes de veículos que queimam combustíveis fósseis como gasolina, diesel, gás natural, etanol e outros.')
    combMovel = input('A empresa faz uso de combustível Móvel? \n [1] - Sim | [0] - Não \n')
    while True:
        if combMovel == '1':
            while True:
                print('Selecione um tipo de combustivel: \n[1] - Etanol \n[2] - Gasolina \n[3] - Diesel \n[4] - BioDiesel \n[5] - glp \n[0] - Sair')
                slComb = str(input())
                if slComb == '1':  
                    etanol.append(float(input('Qual e o consumo médio em litros de Etanol por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combMovel = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '2':
                    gasolina.append(float(input('Qual e o consumo médio em litros de Gasolina por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combMovel = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '3':
                    diesel.append(float(input('Qual e o consumo médio em litros de Diesel por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combMovel = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '4':
                    biodiesel.append(float(input('Qual e o consumo médio em litros de BioDiesel por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
                    if slEscolha == '1':
                        print()
                    elif slEscolha == '0':
                        combMovel = '0'
                        break
                    else:
                        print('Erro: Digite uma opção valida')
                elif slComb == '5':
                    glp.append(float(input('Qual e o consumo médio em litros de GLP (Gás liquefeito de Petrólio) por mês? ')))
                    slEscolha = input('Existe mais tipo de combustível para colocar o consumo? \n [1] - Sim | [0] - Não \n'))
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
    etanol = (((12 * sum(etanol))/1000) * comb['etanol'])
    gasolina = (((12 * sum(gasolina))/1000) * comb['gasolina'])
    diesel = (((12 * sum(diesel))/1000) * comb['diesel'])
    biodiesel = (((12 * sum(biodiesel))/1000) * comb['biodiesel'])
    glp = (((12 * sum(glp))/1000) * comb['glp']) #não finalizado
    #teste
    print(f'Toneladas: {etanol}')
    print(f'Toneladas: {gasolina}')
    print(f'Toneladas: {diesel}')
    print(f'Toneladas: {biodiesel}')
    print(f'Toneladas: {glp}, não finalizado!')

#emissão industrial
    if rmEmpresa == '2':
        print('****** Produção ****** \n [1] - Produção de Aço \n [2] - Produção de Cimento \n [3] - Produção de Papel \n [4] - Produção de Vidro \n [5] - Produção de Alumínio \n [6] - Produção de Amônia \n [7] - Produção de Etanol \n [8] - Produção de Eletricidade a Carvão \n [9] - Produção de Eletricidade a Gás Natural \n [10] - Produção de Eletricidade a Petróleo ')
        prod = input('Selecione o que a empresa produz: \n')
        totalProd = []
        while True:
            if prod == '1':
                prodAco = float(input('Informe a quantidade de aço produzida por dia pela empresa: \n'))
                totalAco = ((((prodAco * 30)*12)/1000) * prodIndustrial[prodAco])
                totalProd.append(totalAco)
                break
            elif prod == '2':
                prodCimento = float(input('Informe a quantidade de cimento produzida por dia pela empresa: \n'))
                totalCimento = ((((prodCimento * 30)*12)/1000) * prodIndustrial[prodCimento])
                totalProd.append(totalCimento)
                break
            elif prod == '3':
                prodPapel = float(input('Informe a quantidade de papel produzida por dia pela empresa: \n'))
                totalPapel = ((((prodPapel * 30)*12)/1000) * prodIndustrial[prodPapel])
                totalProd.append(totalPapel)
                break
            elif prod == '4':
                prodVidro = float(input('Informe a quantidade de vidro produzida por dia pela empresa: \n'))
                totalVidro = ((((prodVidro * 30)*12)/1000) * prodIndustrial[prodVidro])
                totalProd.append(totalVidro)
                break
            elif prod == '5':
                prodAluminio = float(input('Informe a quantidade de Alumínio produzida por dia pela empresa: \n'))
                totalAluminio = ((((prodAluminio * 30)*12)/1000) * prodIndustrial[prodAluminio])
                totalProd.append(totalAluminio)
                break
            elif prod == '6':
                prodAmonia = float(input('Informe a quantidade de Amônia produzida por dia pela empresa: \n'))
                totalAmonia = ((((prodAmonia * 30)*12)/1000) * prodIndustrial[prodAmonia])
                totalProd.append(totalAmonia)
                break
            elif prod == '7':
                prodEtanol = float(input('Informe a quantidade de Etanol produzida por dia pela empresa: \n'))
                totalEtanol = ((((prodEtanol * 30)*12)/1000) * prodIndustrial[prodEtanol])
                totalProd.append(totalEtanol)
                break
            elif prod == '8':
                prodEletricidade_Carvao = float(input('Informe a quantidade de Energia a carvão produzida por dia pela empresa: \n'))
                totalEletricidade_Carvao = ((((prodEletricidade_Carvao * 30)*12)/1000) * prodIndustrial[prodEletricidade_Carvao])
                totalProd.append(totalEletricidade_Carvao)
                break
            elif prod == '9':
                prodEletricidade_GasNat = float(input('Informe a quantidade de Energia a gás natural produzida por dia pela empresa: \n'))
                totalEletricidade_GasNat = ((((prodEletricidade_GasNat * 30)*12)/1000) * prodIndustrial[prodEletricidade_GasNat])
                totalProd.append(totalEletricidade_GasNat)
                break
            elif prod == '10':
                prodEletricidade_Petróleo = float(input('Informe a quantidade de Energia a petróleo produzida por dia pela empresa: \n'))
                totalEletricidade_Petróleo = ((((prodEletricidade_Petróleo * 30)*12)/1000) * prodIndustrial[prodEletricidade_Petróleo])
                totalProd.append(totalEletricidade_Petróleo)
                break
            else:
                print('Erro: Selecione uma opção valida. ')

#emissão fugitivas
    #arcondicionado
    print('As emissões fugitivas ocorrem quando gases de efeito estufa são liberados diretamente na atmosfera a partir de processos produtivos ou equipamentos, como: ar-condicionado, geladeiras, extintores de incêndio e sistemas de armazenamento de gases industriais.')
    ar = input('A empresa possui ar condicionado? \n [1] - Sim | [0] - Não \n')
    while True:
        if ar == '1':
            qtArP = int(input('Quantos Ar condicionado pequeno? \n'))
            hrArP = float(input('Quantas horas em média ele fica ligado? \n'))
            qtArM = int(input('Quantos Ar condicionado mdio? \n'))
            hrArM = float(input('Quantas horas em média ele fica ligado? \n'))
            qtArG = int(input('Quantos Ar condicionado grande? \n'))
            hrArG = float(input('Quantas horas em média ele fica ligado? \n'))
            qtArI = int(input('Quantos Ar condicionado industrial? \n'))
            hrArI = float(input('Quantas horas em média ele fica ligado? \n'))
            break
        elif ar == '0':
            break
        else:
            print('Erro: Digite um valor valido')
    print('Outros Equipamentos')
    qtGeladeira = int(input('Número de geladeiras: ')) #por enquanto meramente ilustrativa
    qtExtintorABC = int(input('Número de Extintor ABC: ')) #por enquanto meramente ilustrativa
    qtExtintorCO2 = int(input('Número de Extintor de CO2: ')) #por enquanto meramente ilustrativa

#calculo Ar Condicionado
    arP = (((((qtArP * hrArP) * 30) * 12) / 1000) * arCond['arPequeno']) #Resultado ar pequeno em toneladas
    arM = (((((qtArM * hrArM) * 30) * 12) / 1000) * arCond['arMedio']) # Resultado ar pequeno em toneladas
    arG = (((((qtArG * hrArG) * 30) * 12) / 1000) * arCond['arGrande']) # Resultado ar pequeno em toneladas
    arI = (((((qtArI * hrArI) * 30) * 12) / 1000) * arCond['arIndustrial']) # Resultado ar pequeno em toneladas
    totalAr = (arP + arM + arG + arI) #resultado total do Ar condicionado

#energia eletrica
    print('Digite o consumo de de energia media gasta por mês: ')
    energia = float(input())
    print('A empresa gera energia solar? \n[1] - Sim | [0] - Não')
    solar = str(input())
    while True:
        if solar == '1':
            print('A energia solar gerada equivale, em média, a que percentual do seu consumo da rede?')
            gerSolar = float(input())
        elif solar == '0':
            break
        else:
            print('Erro: Digite um valor valida')
