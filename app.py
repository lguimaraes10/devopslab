from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True

@app.route('/Hello World - Lucas Guimaraes - FIAP/', methods=['POST']) # Compliant
def pagina_inicial():

    return "Hello World - Lucas Guimaraes - FIAP"

class unprotectedForm(FlaskForm):
    pass
    class Meta:
        csrf = True # Compliant

    name = TextField('name')
    submit = SubmitField('submit')

if __name__ == '__main__':
    app.run()

