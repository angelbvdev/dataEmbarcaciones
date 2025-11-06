from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar modelo
modelo = joblib.load("models/modelo_final.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form
        df = pd.DataFrame([{
            'toneladas': float(data['toneladas']),
            'eslora': float(data['eslora']),
            'calado_maximo': float(data['calado_maximo']),
            'tipo_embarcacion': data['tipo_embarcacion'],
            'densidad_carga': float(data['toneladas']) / (float(data['eslora'])*float(data['manga'])),
            'eficiencia_carga': float(data['toneladas']) / float(data['calado_maximo'])
        }])
        pred = modelo.predict(df)[0]
        return render_template("index.html", pred=round(pred,2))
    return render_template("index.html", pred=None)

if __name__ == "__main__":
    app.run(debug=True)
