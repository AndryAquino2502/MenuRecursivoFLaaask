from flask import Flask, render_template

app = Flask(__name__)

# =============================
# Menú de navegación anidado
# =============================
# Diccionario que representa el menú y sus submenús
menu = {
    "Inicio": {},
    "Oferta Educativa": {
        "Licenciaturas e Ingenierías": {
            "Ing. Sistemas Computacionales": {
                "Plan de Estudios": {},
                "Programa": {}
            },
            "Ing. Electrónica": {
                "Plan de Estudios": {},
                "Programa": {}
            }
        },
        "Posgrado": {}
    },
    "Contacto": {}
}

# =============================
# Ruta principal
# =============================
@app.route("/")
def inicio():
    # Renderiza la plantilla y pasa el menú como contexto
    return render_template("menu.html", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)