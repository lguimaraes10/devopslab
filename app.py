from flask import Flask
from flask_wtf.csrf import CsrfProtect
app = Flask(__name__)
app.secret_key = 'very secret'
CsrfProtect(app)

@app.route('/Hello World - Lucas Guimaraes - FIAP/', methods=['POST']) # Compliant
def pagina_inicial():
    return "Hello World - Lucas Guimaraes - FIAP"

class unprotectedForm(FlaskForm):
    class Meta:
        csrf = True # Compliant

    name = TextField('name')
    submit = SubmitField('submit')

if __name__ == '__main__':
    app.run()

