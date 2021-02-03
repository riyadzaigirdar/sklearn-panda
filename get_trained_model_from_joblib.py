import joblib  # from sklearn.tree import DecisionTreeClassifier in Previous Versions

model = joblib.load("trained_data.joblib")

print(model.predict([[21, 0]]))
