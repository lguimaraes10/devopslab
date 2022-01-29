from flask_wtf.csrf import CsrfProtect
from flask import Flask

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app) # Compliant

@app.route("/")
def pagina_inicial():
    return "Hello World - Lucas Guimaraes - FIAP"

if __name__ == '__main__':
    app.run()
