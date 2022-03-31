from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

@app.route("/")
def pagina_inicial():
    return "Hello World - 30/03/2022 - FIAP"

class unprotectedForm(FlaskForm):
    class Meta:
        csrf = True # Compliant

    name = TextField('name')
    submit = SubmitField('submit')

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)