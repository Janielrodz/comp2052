from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return ("Actividad Módulo 1, actividad 3. Rutas: /info, /crear_usuario, /usuarios")

@app.route("/info", methods=["GET"])
def info():
    carros = {
        "toyota": "SUV",
        "corvette": "Convertible",
        "mercedes": "Wagon"
    }
    return jsonify(carros)

@app.route("/crear_usuario", methods=["POST"])
def crear_usuarios():
    data = request.json
    nombre = data.get("nombre")
    correo_electronico = data.get("correo_electronico")
    lista_usuarios.append({
        "nombre": nombre,
        "correo_electronico": correo_electronico
        })
    
    if not nombre or not correo_electronico:
        return jsonify ({"error": "Datos incompletos"}), 400
    
    return jsonify ({"mensaje": f"Hola, {nombre}! Tu correo electronico es {correo_electronico}"})

lista_usuarios = [{"nombre":"Lebron", "correo_electronico":"lbj23@gmail.com"}]

@app.route("/usuarios", methods=["GET"])
def usuarios():
    return jsonify(lista_usuarios)

if __name__ == "__main__":
    app.run(debug=True)