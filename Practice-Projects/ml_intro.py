import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


music_data = pd.read_csv('music.csv')

feature_names = music_data.columns[:-1]

X = music_data.drop(columns=["genre"])
Y = music_data["genre"]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

predictions = model.predict(X_test)

score = accuracy_score(Y_test, predictions)

plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=feature_names, class_names=model.classes_, filled=True, rounded=True)
plt.show()



