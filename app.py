from flask import Flask, render_template, request
import pickle
from feature_extractor import extract_features

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    url = request.form["url"]

    features = extract_features(url)

    prediction = model.predict([features])

    if prediction[0] == 1:
        result="Phishing Website"
    else:
        result="Legitimate Website"

    return result


if __name__=="__main__":
    app.run()
