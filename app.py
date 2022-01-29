from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True

@app.route('/Hello World - Lucas Guimaraes - FIAP/', methods=['POST']) # Compliant
def pagina_inicial():

    return "Hello World - Lucas Guimaraes - FIAP"

from flask_wtf import FlaskForm
 
class ContactForm(FlaskForm):
   pass
        csrf = True # Compliant

    name = TextField('name')
    submit = SubmitField('submit')

if __name__ == '__main__':
    app.run()

