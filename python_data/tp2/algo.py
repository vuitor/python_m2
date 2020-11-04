import pandas as pd
import sklearn
import joblib 
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
from sklearn.multiclass import OneVsRestClassifier

clf = make_pipeline(
  TfidfVectorizer(stop_words=get_stop_words('en')),
  OneVsRestClassifier(SVC(kernel='linear', probability=True))
)

clf = clf.fit(X=labelDf['tweet'], y=labelDf['class'])

joblib.dump(clf, 'model.pkl')