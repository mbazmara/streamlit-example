import pandas as pd
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.metrics import accuracy_score


def DT_Class(data, class_label, X_train, X_test, Y_train, Y_test):
    model = dtc(max_leaf_nodes=10, max_depth=3)
    model.fit(X_train, Y_train)
    result = model.predict(X_test)
    x = accuracy_score(Y_test, result) * 100
    return x
