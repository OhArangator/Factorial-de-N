from flask import Flask, render_template

app = Flask(__name__)


def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n-1)


@app.route('/')
def home():
    return '¡Calculadora de factorial! \n Usa la URL/factorial/acaElNumero para calcularle su factorial.'



@app.route('/factorial/<int:numero>')
def factorial(numero):
    try:
        if numero < 0:
            return f"Error: No se puede calcular el factorial de un número negativo."
        elif numero > 983:
            return f"Error: El número {numero} es demasiado grande para calcular su factorial."        
        else:
            resultado = calcular_factorial(numero)
        return f"El factorial de {numero} es: {resultado}"
    
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)