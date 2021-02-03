import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz

# dataframe
df = pd.read_csv("music.csv")

# input
X = df.drop(labels=["genre"], axis=1)

# output
Y = df["genre"]

# initializing model
model = DecisionTreeClassifier()

model.fit(X, Y)

export_graphviz(model, out_file="output_tree.dot",
                feature_names=["age", "gender"],
                class_names=sorted(Y.unique()),
                label='all',
                filled=True,
                rounded=True
                )
