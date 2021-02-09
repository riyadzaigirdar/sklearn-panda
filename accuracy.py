from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

df = pd.read_csv("music.csv")

model_object = DecisionTreeClassifier()

x_train, x_test, y_train, y_test = train_test_split(
    df.drop(labels=["genre"], axis=1), df["genre"], test_size=0.2)

# axis 1 mean drop in y axis(column)(column namd) and axis 0 means drop in x axis(row)(index)
# test size 0.2 means 80% of data used for training and 20% will be used for test


model_object.fit(x_train, y_train)  # 80 % input data and 80% output data

predictions = model_object.predict(x_test)  # making predictions

# test accuracy with 20% test output data
score = accuracy_score(y_test, predictions)
print(score)
