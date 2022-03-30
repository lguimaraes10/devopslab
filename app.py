from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

@app.route("/")
def pagina_inicial():
    return "Hello World - Lucas Guimaraes - FIAP"


if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)