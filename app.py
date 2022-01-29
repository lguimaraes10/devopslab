from flask import Flask

app = Flask(__name__)

csrf = CSRFProtect()
csrf.init_app(app) # Compliant

@app.route("/")
def pagina_inicial():
    return "Hello World - Lucas Guimaraes - FIAP"

class unprotectedForm(FlaskForm):
    class Meta:
        csrf = True # Compliant

    name = TextField('name')
    submit = SubmitField('submit')

if __name__ == '__main__':
    app.run()