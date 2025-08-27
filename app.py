from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>Bem-vindo ao Meu Site</h1>
    <nav>
        <ul>
            <li><a href="index.html">Início</a></li>
            <li><a href="sobre.html">Sobre</a></li>
            <li><a href="contato.html">Contato</a></li>
        </ul>
    </nav>

    <h2>Quem somos</h2>
    <p>Este é um site de exemplo feito apenas com HTML, sem CSS.</p>

    <h2>Notícias recentes</h2>
    <ul>
        <li>Notícia 1 - Algo interessante aconteceu!</li>
        <li>Notícia 2 - Confira nossas atualizações.</li>
        <li>Notícia 3 - Mais novidades em breve.</li>
    </ul>

    <footer>
        <p>&copy; 2025 Meu Site. Todos os direitos reservados.</p>
    </footer>
    '''

if __name__ == '__main__':
    app.run()


app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
     app.run()