from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Lucas Guimaraes - FIAP"

if __name__ == '__main__':
    app.run()

from flask_wtf.csrf import CsrfProtect
app = Flask(__name__)
app.secret_key = 'very secret'
CsrfProtect(app)

WTF_CSRF_ENABLED = True