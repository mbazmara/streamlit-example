import pandas as pd
from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.metrics import accuracy_score


def KNN_Class(data, class_label, X_train, X_test, Y_train, Y_test):
    model = knn(n_neighbors=10, p=2, metric='euclidean')
    model.fit(X_train, Y_train)
    result = model.predict(X_test)
    x = accuracy_score(Y_test, result) * 100
    return x