import streamlit as st
from classifiers import DT_classifier as dt
from classifiers import RF_classifier as rf
from classifiers import Categorized as ct
from classifiers import SVM_classifier as svm
from classifiers import KNN_classifier as knn
from sklearn.model_selection import train_test_split as tts
import requests
import pandas as pd

st.set_page_config(page_title='Classify your data', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title("Classify any DataSet you want")
x = st.file_uploader("Pick a file", type=['csv', 'xlsx'])
if x is not None:
#try:
    raw_data = pd.read_csv(x)
    st.title("first 5 insctances of your dataset")
    st.write(raw_data.head(5))
    # learn the dataset and predict it with all pethods
    st.write('---')
    st.title("Results for your dataset")
    data = ct.categorize(raw_data)
    data_size = data.shape
    number_of_instances = data_size[0]
    number_of_features = data_size[1] - 1
    class_label = data.columns[number_of_features]
    data_input = data.drop(columns=[class_label])
    data_target = data[class_label]
    X_train, X_test, Y_train, Y_test = tts(data_input, data_target, test_size=.2)
    accuracy1 = rf.RF_Class(data, class_label, X_train, X_test, Y_train, Y_test)
    accuracy2 = dt.DT_Class(data, class_label, X_train, X_test, Y_train, Y_test)
    accuracy3 = svm.SVM_Class(data, class_label, X_train, X_test, Y_train, Y_test)
    accuracy4 = knn.KNN_Class(data, class_label, X_train, X_test, Y_train, Y_test)
    st.subheader(f'Accuracy of RandomForest is {accuracy1}')
    st.subheader(f'Accuracy of DecisionTree is {accuracy2}')
    st.subheader(f'Accuracy of SVM is {accuracy3}')
    st.subheader(f'Accuracy of KNN(k=10) is {accuracy4}')
#except Exception as e:
#    st.write(e)
#    st.write('please upload your dataset')
#except ValueError as v:
#    st.write(v)
