import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv("Day15/DataSet_Titanic.csv")

X = df.drop("Sobreviviente", axis=1)

y = df.Sobreviviente


arbol = DecisionTreeClassifier(max_depth=2, random_state=42)

arbol.fit(X, y)

pred_y = arbol.predict(X)

print("Precision: ", accuracy_score(pred_y, y))

print(confusion_matrix(y, pred_y))

ConfusionMatrixDisplay.from_estimator(arbol, X, y, cmap=plt.cm.Blues, values_format='.0f')
plt.show()

ConfusionMatrixDisplay.from_estimator(arbol, X, y, cmap=plt.cm.Blues, values_format='.2f', normalize='true')
plt.show()

plt.figure(figsize=(10,8))
tree.plot_tree(arbol, filled=True, feature_names=X.columns)
plt.show()

importancias = arbol.feature_importances_
columnas = X.columns

sns.barplot(importancias)
plt.title('Importancia de cada atributo')
plt.show()
