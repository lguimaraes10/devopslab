from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True
csrf = CSRFProtect()
csrf.init_app(app)

@app.route("/")
def pagina_inicial():
    return "Hello World - Lucas Guimaraes - FIAP"

if __name__ == '__main__':
    app.run()

