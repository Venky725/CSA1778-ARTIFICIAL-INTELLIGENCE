from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data
Y = iris.target

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

clf=DecisionTreeClassifier()

clf.fit(X_train,Y_train)

Y_pred=clf.predict(X_test)

accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy :",accuracy)
