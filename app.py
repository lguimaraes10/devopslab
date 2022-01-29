from flask import Flask

app = Flask(__name__)
csrf = False
csrf.init_app() # Compliant

@app.route('/Hello World - Lucas Guimaraes - FIAP/', methods=['POST']) # Compliant
def pagina_inicial():
    return "Hello World - Lucas Guimaraes - FIAP"

if __name__ == '__main__':
    app.run()

