from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn
import sklearn

app = FastAPI()
model = joblib.load("model_resultat.pkl")

# Classe pour faciliter les appels de donnees ou les 2 models
class Tweet(BaseModel):
    tweet = str

# Création des rêquetes et des routes qui seront appelées par une URL (localhost:NUMERO_DU_PORT/)
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Récuperation des donnees du model resultat et la route URL (localhost:NUMERO_DU_PORT/dataTweet/MOT_A_TESTER)
@app.get("/dataTweet/{tweet}")
def get_offensive_language(tweet): 
    if (tweet) :
        Y_pred = model.predict_proba([tweet])[0]

        if Y_pred[0] > Y_pred[1] and Y_pred[0]> Y_pred[2]:
            return("hate_speech")
        elif Y_pred[1] > Y_pred[0] and Y_pred[1]> Y_pred[2]:
            return("offensive_language")
        else :
            return("neither")