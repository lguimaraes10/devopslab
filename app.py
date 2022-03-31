from flask import Flask

app = Flask(__name__)

csrf = CSRFProtect(app)
csrf.init_app(app) # Compliant

@app.route("/")
def pagina_inicial():
    return "Hello World - 30/03/2022 - FIAP"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)