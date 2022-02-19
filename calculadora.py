from flask import Flask, render_template, request

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/calcular', methods=['POST', 'GET'])
def calcular():
    valor1 = request.form["v1"]
    valor2 = request.form["v2"]
    operador = request.form['operacao']

    if (operador == "soma"):
        result = int(valor1) + int(valor2)

    elif(operador == "subtracao"):
        result = int(valor1) - int(valor2)

    elif(operador == "divisao"):
        result = int(valor1) / int(valor2)

    elif(operador == "multiplicacao"):
        result = int(valor1) * int(valor2)

    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
