import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
gre = pd.read_csv("3admission.csv")
gre.head()
print(gre)
gre.describe
gre=gre.rename(columns={"TOEFL Score":"TOEFL"})
gre=gre.rename(columns={"University Rating":"univ_rating"})
gre=gre.rename(columns={"Serial No.":"ID"})
gre=gre.rename(columns={"Chance of Admit ":"Admission chance"})
gre.columns
sns.pairplot(data=gre)
plt.figure(figsize=(12,12))
sns.lineplot(data=gre, x="GRE Score",y="TOEFL", hue="Research")
plt.figure(figsize=(12,12))
h = sns.scatterplot(data=gre, x="CGPA", y="ID", hue="Research")
s = sns.FacetGrid(data = gre, col="Research", row="univ_rating", hue="LOR ")
s.map(sns.scatterplot, "CGPA","ID")
s.add_legend()

sns.catplot(data=gre, x="Research", y="Admission chance", hue="univ_rating")
plt.figure(figsize=(12,12))
sns.heatmap(gre.corr(), annot=True,cmap="cubehelix")
from sklearn.model_selection import train_test_split
a = gre.drop("Admission chance", axis =1)
b = gre["Admission chance"]
a
b
a_train,a_test,b_train,b_test = train_test_split(a,b, test_size=0.2, random_state=1)
from sklearn import linear_model
lr = linear_model.LinearRegression()
lr.fit(a_train,b_train)
pred = lr.predict(a_test)
from sklearn.metrics import classification_report, confusion_matrix, r2_score
lr.intercept_
coef = pd.DataFrame(lr.coef_, a.columns, columns = ['coef'])
coef
r2 = r2_score(b_test, pred)
print("r2 score:" ,r2)
predd = pd.DataFrame(pred)
frames = [gre,predd]
pred_values = pd.concat(frames, axis=1)
pred_values.columns
pred_values.head()
