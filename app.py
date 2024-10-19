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
    'ProdAco': 1.8,  # kg de co2 por kg produzido
    'ProdCimento': 0.9,  # kg de co2 por kg produzido
    'ProdPapel': 0.5,  # kg de co2 por kg produzido
    'ProdVidro': 0.6,  # kg de co2 por kg produzido
    'ProdAluminio': 12,  # kg de co2 por kg produzido
    'ProdAmonia': 1.8,  # kg de co2 por kg produzido
    'ProdEtanol': 1.6,  # kg de co2 por kg produzido
    'ProdEletricidade_Carvao': 0.9,  # kg de co2 por kg produzido
    'ProdEletricidade_GasNat': 0.4,  # kg de co2 por kg produzido
    'ProdEletricidade_Petróleo': 0.7  # kg de co2 por kg produzido
}
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

    #entrada dos dados via formulario
    etanol = float(request.form['etanol'])
    gasolina = float(request.form['gasolina'])
    diesel = float(request.form['diesel'])
    biodiesel = float(request.form['biodiesel'])

    #calculo combustível
    etanol = (((12 * etanol)/1000) * comb['etanol'])
    gasolina = (((12 * gasolina)/1000) * comb['gasolina'])
    diesel = (((12 * diesel)/1000) * comb['diesel'])
    biodiesel = (((12 * biodiesel)/1000) * comb['biodiesel'])
    combTotal = (etanol + gasolina + diesel + biodiesel)

    #calculo produção
    ProdAco = float(request.form['ProdAco'])
    ProdCimento = float(request.form['ProdCimento'])
    ProdPapel = float(request.form['ProdPapel'])
    ProdVidro = float(request.form['ProdVidro'])
    ProdAluminio = float(request.form['ProdAluminio'])
    ProdEtanol = float(request.form['ProdEtanol'])
    ProdAmonia = float(request.form['ProdAmonia'])
    ProdEtanol = float(request.form['ProdEtanol'])
    ProdEletricidade_Carvao = float(request.form['ProdEletricidade_Carvao'])
    ProdEletricidade_GasNat = float(request.form['ProdEletricidade_GasNat'])
    ProdEletricidade_Petroleo = float(request.form['ProdEletricidade_Petroleo'])

    #retorno
    mensagem = dadosEmpresa
    mensagem2 = (f'Emissão total combustível: {combTotal:.2f}Toneladas co2')
    return render_template('company_results.html',
                           nome_empresa=dadosEmpresa['nome'],
                           endereco_empresa=dadosEmpresa['endereco'],
                           nomeResponsavel_empresa=dadosEmpresa['nomeResponsavel'],
                           telefoneResponsavel_empresa=dadosEmpresa['telefoneResponsavel'],
                           ano_inventariado=dadosEmpresa['anoInventariado'],ramo_empresa=dadosEmpresa['ramoEmpresa'],)


@app.route('/submit2', methods=['POST'])
def submit2():
    nome_pessoa = request.form['nome_pessoa']
    email_pessoa = request.form['email_pessoa']
    idade_pessoa = request.form['idade_pessoa']
    return f'Nome: {nome_pessoa}, Email: {email_pessoa}, Idade: {idade_pessoa}'

if __name__ == '__main__':
    app.run(debug=True)


