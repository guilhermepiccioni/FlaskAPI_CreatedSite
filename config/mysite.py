from flask import Flask, render_template, request


from config.models import get_pessoas, criar_post

app = Flask(__name__)


# Eliminando o erro


@app.route('/<string:nome>')
def error(nome):
    variavel = f'''Página {nome.upper()} não encontrada!'''
    return render_template("error.html", variavel=variavel)


@app.route('/', methods=["GET", "POST"])
def index():
    apresentacao = '''Olá, me chamo Elon Musk.'''
    boas_vindas = 'Seja bem vindo(a) ao meu site de iniciante.'
    texto1 = 'Coloque os dados abaixo para se cadastrar em meu Banco de Dados.'
    cadastro = f'Parabéns. Cadastro efetuado com Sucesso!'

    if request.method == 'GET':
        pass

    if request.method == 'POST':
        nome = request.form.get('name')
        sobrenome = request.form.get('surname')
        email = request.form.get('email')
        criar_post(nome, sobrenome, email)

    pessoas = get_pessoas()

    return render_template("index.html", apresentacao=apresentacao,
                           boas_vindas=boas_vindas, texto1=texto1, pessoas=pessoas, cadastro=cadastro)


@app.route('/about')
def about():
    quem_sou = 'Elon Musk'
    bibliografia = """Elon Reeve Musk, FRS (Pretória, 28 de junho de 1971) é um empreendedor e filantropo 
    sul-africano-canadense-americano. Ele é o fundador, CEO e CTO da SpaceX; CEO da Tesla Motors; vice-presidente da 
    OpenAI, fundador e CEO da Neuralink e co-fundador e presidente da SolarCity. Em 7 de janeiro de 2021, com um 
    patrimônio pessoal estimado em cerca de 188,5 bilhões de dólares, tornou-se a pessoa mais rica do mundo, de acordo 
    com a Bloomberg, ultrapassando o empresário Jeff Bezos. No ranking da Forbes, Musk ocupa o segundo lugar."""
    return render_template("about.html", bibliografia=bibliografia, quem_sou=quem_sou)


if __name__ == '__main__':
    app.run(debug=True)
