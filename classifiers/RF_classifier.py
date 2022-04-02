import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.metrics import accuracy_score


def RF_Class(data, class_label, X_train, X_test, Y_train, Y_test):
    model = rfc(n_estimators=50, min_samples_leaf=2)
    model.fit(X_train, Y_train)
    result = model.predict(X_test)
    x = accuracy_score(Y_test, result) * 100
    return x