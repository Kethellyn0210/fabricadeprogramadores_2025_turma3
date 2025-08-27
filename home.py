from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '''
 <h1>Sobre Nós</h1>
    <p>Bem-vindo à nossa página sobre. Aqui você pode aprender mais sobre quem somos e o que fazemos.</p>
    
    <h2>Nossa História</h2>
    <p>Fundamos nossa empresa em 2020 com o objetivo de oferecer soluções inovadoras para nossos clientes.</p>
    
    <h2>Missão</h2>
    <p>Proporcionar qualidade, confiança e satisfação em todos os nossos serviços.</p>
    
    <h2>Equipe</h2>
    <ul>
        <li>João Silva - CEO</li>
        <li>Maria Oliveira - Diretora de Marketing</li>
        <li>Carlos Souza - Desenvolvedor</li>
    </ul>
    
    <h2>Contato</h2>
    <p>Você pode entrar em contato conosco pelo e-mail: contato@exemplo.com</p>
 '''

if __name__ == '__main__':
    app.run()


app.add_url_rule('/', 'index', index)

if __name__ == '__main__':
     app.run()