import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib  # from sklearn.tree import DecisionTreeClassifier in Previous Versions

df = pd.read_csv("music.csv")

model = DecisionTreeClassifier()

X = df.drop(labels=["genre"], axis=1)
Y = df["genre"]

model.fit(X, Y)

joblib.dump(model, "trained_data.joblib")
