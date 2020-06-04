import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import os
os.chdir('F:\\Program Files\\program')
df=pd.read_csv('news.csv')
#Get shape and head
#print(df.head())
labels=df.label
x_train,x_test,y_train,y_test=train_test_split(df['text'], labels, test_size=0.3, random_state=7)
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_train=tfidf_vectorizer.fit_transform(x_train) 
tfidf_test=tfidf_vectorizer.transform(x_test)
pac=PassiveAggressiveClassifier(max_iter=75)
pac.fit(tfidf_train,y_train)
y_pred=pac.predict(tfidf_test)
print(y_pred)
score=accuracy_score(y_test,y_pred)
print(score)
feature_names  =  tfidf_vectorizer . get_feature_names ()
hash_vectorizer = HashingVectorizer(stop_words='english')
hash_train = hash_vectorizer.fit_transform(x_train)
hash_test = hash_vectorizer.transform(x_test)
pac.fit(hash_train,y_train)
y_pred_1=pac.predict(hash_test)
score1=accuracy_score(y_test,y_pred_1)
print(f"Accuracy with Hashing vectorizer :{round(score1*100,2)}%")
print(f'Accuracy with tf-idf vectorizer: {round(score*100,2)}%')
print(classification_report(y_pred_1,y_test))
print(classification_report(y_pred,y_test))
print(confusion_matrix(y_pred_1,y_test))
print(confusion_matrix(y_pred,y_test))
