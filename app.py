#IMPORTS FLASK
from flask import Flask, render_template, request
#IMPORTS ML
import joblib

app = Flask(__name__)
#necessário para o funcionamento da ML
model = joblib.load(open("models/sales.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        valor1 = float(request.form["tv"].replace(',', '.'))
        valor2 = float(request.form["jornal"].replace(',', '.'))
        valor3 = float(request.form["radio"].replace(',', '.'))

        #Fazendo uso da ML
        prediction = model.predict([[valor1, valor2, valor3]])
        f_prediction1 = round(prediction[0], 2)

        return render_template("saída.html", prediction=str(f_prediction1).replace('.', ','))
    else:
        return render_template("entrada.html")

if __name__ == "__main__":
    app.run(debug=True)