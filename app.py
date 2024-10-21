from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Base de dados "Fator de conversão"
comb = {
    'etanol': 1.94,  # CO2/litro
    'gasolina': 2.31,  # CO2/litro
    'diesel': 2.68,  # CO2/litro
    'biodiesel': 2.46,  # CO2/litro
    'glp': 2.50  # CO2/litro
}
arCond = {
    'arPequeno': 0.5,  # kg por hora
    'arMedio': 1.5,  # kg por hora
    'arGrande': 3,  # kg por hora
    'arIndustrial': 4  # kg por hora
}

prodIndustrial = {
    'prodAco': 1.8,  # kg de co2 por kg produzido
    'prodCimento': 0.9,  # kg de co2 por kg produzido
    'prodPapel': 0.5,  # kg de co2 por kg produzido
    'prodVidro': 0.6,  # kg de co2 por kg produzido
    'prodAluminio': 12,  # kg de co2 por kg produzido
    'prodAmonia': 1.8,  # kg de co2 por kg produzido
    'prodEtanol': 1.6,  # kg de co2 por kg produzido
    'prodEletricidade_Carvao': 0.9,  # kg de co2 por kg produzido
    'prodEletricidade_GasNat': 0.4,  # kg de co2 por kg produzido
    'prodEletricidade_Petroleo': 0.7  # kg de co2 por kg produzido
}

totalEmissao = []
totalCredito = []

@app.route('/Empresa', methods=['POST'])
def empresa():
    # cadastro empresa
    dadosEmpresa = {}
    dadosEmpresa['nome'] = request.form['nome_empresa'] # Entrada do nome da empresa via formulário
    dadosEmpresa['endereco'] = request.form["endereco_empresa"] # Entrada do endereço da empresa via formulário
    dadosEmpresa['nomeResponsavel'] = request.form['nomeResponsavel_empresa'] # Entrada do nome do responsável pela empresa via formulário
    dadosEmpresa['telefoneResponsavel'] = request.form['telefoneResponsavel_empresa'] # Entrada do telefone do responsavel pela empresa via formulário
    dadosEmpresa['anoInventariado'] = int(request.form['ano_inventariado']) # Entrada do ano de inventario via seleção no formulário
    dadosEmpresa['ramoEmpresa'] = int(request.form['ramo_empresa']) # Entrada do ramo da empresa via seleção do formulário

    #entrada combustivel via formulário
    gasolina = float(request.form['gasolina']) # Entrada do consumo médio de gasolina por veiculo no mês
    qtGasolina = int(request.form['qtGasolina']) # Entrada da quantidade de veiculo a gasolina que a empresa possui
    etanol = float(request.form['etanol']) # Entrada do consumo médio de etanol por veiculo no mês
    qtEtanol = float(request.form['qtEtanol']) # Entrada da quantidade de veiculo a etanol que a empresa possui
    diesel = float(request.form['diesel']) # Entrada do consumo médio de diesel por veiculo no mês
    qtDiesel = float(request.form['qtDiesel']) # Entrada da quantidade de veiculo a disel que a empresa possui
    biodiesel = float(request.form['biodiesel']) # Entrada do consumo médio de biodiesel por veiculo no mês
    qtBiodiesel = float(request.form['qtBiodiesel']) # Entrada da quantidade de veiculo a biodiesel que a empresa possui
    
    #Entrada produção via formulário
    prodAco = float(request.form['ProdAco']) # Entrada da produção de aço em kg/mês
    prodCimento = float(request.form['ProdCimento']) # Entrada da produção de aço em kg/mês
    prodPapel = float(request.form['ProdPapel']) # Entrada da produção de aço em kg/mês
    prodVidro = float(request.form['ProdVidro']) # Entrada da produção de aço em kg/mês
    prodAluminio = float(request.form['ProdAluminio']) # Entrada da produção de aço em kg/mês
    prodEtanol = float(request.form['ProdEtanol']) # Entrada da produção de aço em kg/mês
    prodAmonia = float(request.form['ProdAmonia']) # Entrada da produção de aço em kg/mês
    prodEtanol = float(request.form['ProdEtanol']) # Entrada da produção de aço em kg/mês
    prodEletricidade_Carvao = float(request.form['ProdEletricidade_Carvao']) # Entrada da produção de aço em kg/mês
    prodEletricidade_GasNat = float(request.form['ProdEletricidade_GasNat']) # Entrada da produção de aço em kg/mês
    prodEletricidade_Petroleo = float(request.form['ProdEletricidade_Petroleo']) # Entrada da produção de aço em kg/mês

    #entrada ar condicionado via terminal
    arP = float(request.form['arP']) # entrada do uso do ar condicionado em hr/dia
    qtarP = int(request.form['qtarP']) # quantidade de ar condicionado
    arM = float(request.form['arM']) # entrada do uso do ar condicionado em hr/dia
    qtarM = int(request.form['qtarM']) # quantidade de ar condicionado
    arG = float(request.form['arG']) # entrada do uso do ar condicionado em hr/dia
    qtarG = int(request.form['qtarG']) # quantidade de ar condicionado
    arI = float(request.form['arI']) # entrada do uso do ar condicionado em hr/dia
    qtarI = int(request.form['qtarI']) # quantidade de ar condicionado

    #Processamento dos dados
    totalEmissao.append(((((gasolina * qtGasolina) * 12) * comb['gasolina'])/1000)) # calculo de emissão por queima de gasolina em t/ano
    totalEmissao.append(((((etanol * qtEtanol) * 12) * comb['etanol'])/1000)) # calculo de emissão por queima de etanol em t/ano
    totalEmissao.append(((((diesel * qtDiesel) * 12) * comb['diesel'])/1000)) # calculo de emissão por queima de diesel em t/ano
    totalEmissao.append(((((biodiesel * qtBiodiesel) * 12) * comb['biodiesel'])/1000)) # calculo de emissão por queima de biodiesel em t/ano

    totalEmissao.append(((((prodAco * 30)*12) * prodIndustrial['prodAco'])/1000)) # Calculo de produção de aço em t/ano
    totalEmissao.append(((((prodCimento * 30)*12) * prodIndustrial['prodCimento'])/1000)) # Calculo de produção de cimento em t/ano
    totalEmissao.append(((((prodPapel * 30)*12) * prodIndustrial['prodPapel'])/1000)) # Calculo de produção de papel em t/ano
    totalEmissao.append(((((prodVidro * 30)*12) * prodIndustrial['prodVidro'])/1000)) # Calculo de produção de vidro em t/ano
    totalEmissao.append(((((prodAluminio * 30)*12) * prodIndustrial['prodAluminio'])/1000)) # Calculo de produção de alumínio em t/ano
    totalEmissao.append(((((prodAmonia * 30)*12) * prodIndustrial['prodAmonia'])/1000)) # Calculo de produção de amônia em t/ano
    totalEmissao.append(((((prodEtanol * 30)*12) * prodIndustrial['prodEtanol'])/1000)) # Calculo de produção de etanol em t/ano
    totalEmissao.append(((((prodEletricidade_Carvao * 30)*12) * prodIndustrial['prodEletricidade_Carvao'])/1000)) # Calculo de produção de eletricidade por queima de carvão em t/ano
    totalEmissao.append(((((prodEletricidade_GasNat * 30)*12) * prodIndustrial['prodEletricidade_GasNat'])/1000)) # Calculo de produção de eletricidade por queima de gás natural em t/ano
    totalEmissao.append(((((prodEletricidade_Petroleo * 30)*12) * prodIndustrial['prodEletricidade_Petroleo'])/1000)) # Calculo de produção de eletricidade por queima de petrólio em t/ano

    totalEmissao.append((((((qtarP * arP) * 30) * 12) * arCond['arPequeno']) / 1000)) # Calculo de emissão para ar cond.pequeno em t/ano
    totalEmissao.append((((((qtarM * arM) * 30) * 12) * arCond['arMedio']) / 1000)) # Calculo de emissão para ar cond.pequeno em t/ano
    totalEmissao.append((((((qtarG * arG) * 30) * 12) * arCond['arGrande']) / 1000)) # Calculo de emissão para ar cond.grande em t/ano
    totalEmissao.append((((((qtarI * arI) * 30) * 12) * arCond['arIndustrial']) / 1000)) # Calculo de emissão para ar cond.industrial em t/ano

    #retorno
    mensagem2 = (f'{sum(totalEmissao):.2f}')
    return render_template('company_results.html',
                           nome_empresa=dadosEmpresa['nome'],
                           endereco_empresa=dadosEmpresa['endereco'],
                           nomeResponsavel_empresa=dadosEmpresa['nomeResponsavel'],
                           telefoneResponsavel_empresa=dadosEmpresa['telefoneResponsavel'],
                           ano_inventariado=dadosEmpresa['anoInventariado'],
                           ramo_empresa=dadosEmpresa['ramoEmpresa'],
                           mensagem2=mensagem2)


@app.route('/submit2', methods=['POST'])
def submit2():
    nome_pessoa = request.form['nome_pessoa']
    email_pessoa = request.form['email_pessoa']
    idade_pessoa = request.form['idade_pessoa']
    return f'Nome: {nome_pessoa}, Email: {email_pessoa}, Idade: {idade_pessoa}'

if __name__ == '__main__':
    app.run(debug=True)


