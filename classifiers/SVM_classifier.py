import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


def SVM_Class(data, class_label, X_train, X_test, Y_train, Y_test):
    model = SVC()
    model.fit(X_train, Y_train)
    result = model.predict(X_test)
    x = accuracy_score(Y_test, result) * 100
    return x