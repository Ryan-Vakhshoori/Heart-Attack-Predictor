# flask --app app run

from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

RF_model = pickle.load(open("RF_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    d = {
        "age": [int(request.form.get("age"))],
        "sex": [int(request.form.get("sex"))],
        "cp": [int(request.form.get("cp"))],
        "trtbps": [int(request.form.get("trtbps"))],
        "chol": [int(request.form.get("chol"))],
        "fbs": [int(request.form.get("fbs"))],
        "restecg": [int(request.form.get("restecg"))],
        "thalachh": [int(request.form.get("thalachh"))],
        "exng": [int(request.form.get("exng"))],
        "oldpeak": [float(request.form.get("oldpeak"))],
        "slp": [int(request.form.get("slp"))],
        "caa": [int(request.form.get("caa"))],
        "thall": [int(request.form.get("thall"))],
    }
    df = pd.DataFrame(data=d, index=[0])
    pred = RF_model.predict(df)
    if pred == [1]:
        result =  'more chance of heart attack'
    else:
        result = 'less chance of heart attack'

    return render_template('result.html', prediction=result)
    

    