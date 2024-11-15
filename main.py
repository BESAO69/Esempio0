from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello from Flask!'

@app.route('/prova')
def prova():
    return '<h1>Pagina di Prova</h1>'

app.run(host='localhost', port=3000, debug=True)