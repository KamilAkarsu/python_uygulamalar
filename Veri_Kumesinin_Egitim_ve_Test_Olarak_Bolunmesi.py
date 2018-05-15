#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 13:44:36 2018

@author: kamilakarsu
"""

#Veri Kümesinin Eğitim ve Test Olarak Bölünmesi

import pandas as pd

veriler = pd.read_csv('./data/veriler.csv')
print(veriler)

#---------------------------------------------------------------------------------------------------
ulke = veriler.iloc[:,0:1].values
print(ulke)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0])
print(ulke)
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
ulke=ohe.fit_transform(ulke).toarray()

sonuc1 = pd.DataFrame(data = ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc1)
#---------------------------------------------------------------------------------------------------
Yas = veriler.iloc[:,1:4].values
sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

#---------------------------------------------------------------------------------------------------
cinsiyet = veriler.iloc[:,-1].values
sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])
print(sonuc3)
#---------------------------------------------------------------------------------------------------

s = pd.concat([sonuc1,sonuc2], axis=1)
print(s)
s2 = pd.concat([s,sonuc3], axis=1)
print(s2)


from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(s,sonuc3,test_size=0.33,random_state=0)
print(x_train)

