from flask import Flask, render_template, request

calculadora = Flask(__name__)

@calculadora.route('/')
def index():
    return render_template('calculadora.html')

@calculadora.route('/calcular', methods=['POST'])
def calcular():
    try:
        operacao = request.form['operacao']
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
    except ValueError:
        return render_template('calculadora.html', resultado="Erro: Insira números válidos!")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            return render_template('calculadora.html', resultado="Erro: Divisão por zero!")
    else:
        return render_template('calculadora.html', resultado="Erro: Operação inválida!")

    return render_template('calculadora.html', resultado=f"O resultado é: {resultado}")

if __name__ == '__main__':
    calculadora.run(debug=True)