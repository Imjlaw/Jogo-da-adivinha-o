from flask import Flask, request, render_template
import random

app = Flask(__name__)

numero_secreto = random.randint(1, 100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adivinhar', methods=['POST'])
def adivinhar():
    tentativa = int(request.form['tentativa'])

    if tentativa < numero_secreto:
        resultado = "Tente um número maior."
    elif tentativa > numero_secreto:
        resultado = "Tente um número menor."
    else:
        resultado = f"Parabéns! Você acertou o número secreto {numero_secreto}."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)