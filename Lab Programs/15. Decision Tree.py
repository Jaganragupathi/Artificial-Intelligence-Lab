
from sklearn.tree import DecisionTreeClassifier

X = [[1, 1], [1, 0], [0, 1], [0, 0]]
y = ["Yes", "Yes", "No", "No"]

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

a = int(input("Enter feature 1 (0 or 1): "))
b = int(input("Enter feature 2 (0 or 1): "))

print("Prediction:", model.predict([[a, b]])[0])
