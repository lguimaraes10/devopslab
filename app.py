from flask import Flask
from flask_wtf.csrf import CsrfProtect
app = Flask(__name__)
class Config:
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'

@app.route('/Hello World - Lucas Guimaraes - FIAP/', methods=['POST']) # Compliant
def pagina_inicial():
    return "Hello World - Lucas Guimaraes - FIAP"

if __name__ == '__main__':
    app.run()

