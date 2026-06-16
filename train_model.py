import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier

from feature_extractor import extract_features

df = pd.read_csv("phishing_urls.csv")

X = []

for url in df['url']:
    X.append(extract_features(url))

y = df['label']

model = RandomForestClassifier()

model.fit(X,y)

joblib.dump(model,"model/phishing_model.pkl")

print("Model Trained Successfully")
