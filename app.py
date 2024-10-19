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
@app.route('/Empresa', methods=['POST'])
def empresa():
    # cadastro empresa
    dadosEmpresa = {}
    dadosEmpresa['nome'] = request.form['nome_empresa'] #entrada do nome da empresa via formulário
    dadosEmpresa['endereco'] = request.form["endereco_empresa"] #entrada do endereço da empresa via formulário
    dadosEmpresa['nomeResponsavel'] = request.form['nomeResponsavel_empresa'] #entrada do nome do responsável pela empresa via formulário
    dadosEmpresa['telefoneResponsavel'] = request.form['telefoneResponsavel_empresa'] #entrada do telefone do responsavel pela empresa via formulário
    dadosEmpresa['anoInventariado'] = int(request.form['ano_inventariado'])
    dadosEmpresa['ramoEmpresa'] = int(request.form['ramo_empresa'])

    #entrada combustivel via formulário
    etanol = float(request.form['etanol'])
    gasolina = float(request.form['gasolina'])
    diesel = float(request.form['diesel'])
    biodiesel = float(request.form['biodiesel'])

    #Entrada produção via formulário
    prodAco = float(request.form['ProdAco'])
    prodCimento = float(request.form['ProdCimento'])
    prodPapel = float(request.form['ProdPapel'])
    prodVidro = float(request.form['ProdVidro'])
    prodAluminio = float(request.form['ProdAluminio'])
    prodEtanol = float(request.form['ProdEtanol'])
    prodAmonia = float(request.form['ProdAmonia'])
    prodEtanol = float(request.form['ProdEtanol'])
    prodEletricidade_Carvao = float(request.form['ProdEletricidade_Carvao'])
    prodEletricidade_GasNat = float(request.form['ProdEletricidade_GasNat'])
    prodEletricidade_Petroleo = float(request.form['ProdEletricidade_Petroleo'])

    #entrada ar condicionado via terminal
    arP = float(request.form['arP'])
    qtarP = int(request.form['qtarP'])
    arM = float(request.form['arM'])
    qtarM = int(request.form['qtarM'])
    arG = float(request.form['arG'])
    qtarG = int(request.form['qtarG'])
    arI = float(request.form['arI'])
    qtarI = int(request.form['qtarI'])

    #calculo combustível
    totalEmissao.append((((12 * etanol) * comb['etanol'])/1000))
    totalEmissao.append((((12 * gasolina) * comb['gasolina'])/1000))
    totalEmissao.append((((12 * diesel) * comb['diesel'])/1000))
    totalEmissao.append((((12 * biodiesel) * comb['biodiesel'])/1000))

    #calculo produção
    totalEmissao.append(((((prodAco * 30)*12) * prodIndustrial['prodAco'])/1000))
    totalEmissao.append(((((prodCimento * 30)*12) * prodIndustrial['prodCimento'])/1000))
    totalEmissao.append(((((prodPapel * 30)*12) * prodIndustrial['prodPapel'])/1000))
    totalEmissao.append(((((prodVidro * 30)*12) * prodIndustrial['prodVidro'])/1000))
    totalEmissao.append(((((prodAluminio * 30)*12) * prodIndustrial['prodAluminio'])/1000))
    totalEmissao.append(((((prodAmonia * 30)*12) * prodIndustrial['prodAmonia'])/1000))
    totalEmissao.append(((((prodEtanol * 30)*12) * prodIndustrial['prodEtanol'])/1000))
    totalEmissao.append(((((prodEletricidade_Carvao * 30)*12) * prodIndustrial['prodEletricidade_Carvao'])/1000))
    totalEmissao.append(((((prodEletricidade_GasNat * 30)*12) * prodIndustrial['prodEletricidade_GasNat'])/1000))
    totalEmissao.append(((((prodEletricidade_Petroleo * 30)*12) * prodIndustrial['prodEletricidade_Petroleo'])/1000))

    #calculo Ar condicionado
    totalEmissao.append((((((qtarP * arP) * 30) * 12) * arCond['arPequeno']) / 1000)) #Resultado ar pequeno em toneladas
    totalEmissao.append((((((qtarM * arM) * 30) * 12) * arCond['arMedio']) / 1000)) # Resultado ar pequeno em toneladas
    totalEmissao.append((((((qtarG * arG) * 30) * 12) * arCond['arGrande']) / 1000)) # Resultado ar pequeno em toneladas
    totalEmissao.append((((((qtarI * arI) * 30) * 12) * arCond['arIndustrial']) / 1000)) # Resultado ar pequeno em toneladas

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


