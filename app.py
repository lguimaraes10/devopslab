from flask import Flask

app = Flask(__name__)

@app.route('/example/', methods=['POST']) # Compliant
def example():
    return 'example'

if __name__ == '__main__':
    app.run()

