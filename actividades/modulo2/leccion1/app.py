from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/jugadores/Barcelona")
def barcelona():
    jugadores = [
        {"nombre": "Robert Lewandowski", "posición": "Delantero", "goles": 40, "asistencias": 3},
        {"nombre": "Raphinha", "posición": "Delantero", "goles": 30, "asistencias": 21},
        {"nombre": "Lamine Yamal", "posición": "Delantero", "goles": 14, "asistencias": 18}
    ]
    return render_template('Barcelona.html', jugadores=jugadores)


@app.route("/jugadores/RealMadrid")
def RealMadrid():
    jugadores = [
        {"nombre": "Kylian Mbappé", "posición": "Delantero", "goles": 33, "asistencias": 5},
        {"nombre": "Vinicius JR", "posición": "Delantero", "goles": 21, "asistencias": 12},
        {"nombre": "Jude Bellingham", "posición": "Mediocampista", "goles": 13, "asistencias": 12}
    ]
    return render_template('RealMadrid.html', jugadores=jugadores)
if __name__ == "__main__":
    app.run(debug=True)