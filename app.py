from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Lucas Guimaraes - FIAP"

if __name__ == '__main__':
    app.run()

    class unprotectedForm(FlaskForm):
    class Meta:
        csrf = True

         name = TextField('name')
    submit = SubmitField('submit')