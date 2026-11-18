from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():
    return jsonify({
        "asistente": "FRIDAY",
        "estado": "En línea",
        "mensaje": "Hola, soy FRIDAY. Estoy lista."
    })

@app.route("/estado")
def estado():
    return jsonify({
        "estado": "Funcionando"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
