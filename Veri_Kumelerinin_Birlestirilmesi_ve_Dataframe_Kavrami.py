#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:22:03 2018

@author: kamilakarsu
"""
#Veri Kümelerinin Birleştirilmesi ve Dataframe Kavramı

import pandas as pd

veriler = pd.read_csv('./data/veriler.csv')
print(veriler)
#---------------------------------------------------
ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0])
print(ulke)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(categorical_features='all')
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)


sonuc1 = pd.DataFrame(data = ulke, index = range(22), columns = ['fr','tr','us'])
#sonuc1 adında verisi ulke,kolon isimleri fr-tr-us olan 0-21 indislik DataFrame oluşturduk
print(sonuc1)
#---------------------------------------------------
Yas = veriler.iloc[:,1:4].values
#Yas içinde boy-kilo-yaş var
print(Yas)

sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns = ['boy','kilo','yas'])
#sonuc2 adında verisi Yas,kolon isimleri boy-kilo-yaş olan 0-21 indislik DataFrame oluşturduk
print(sonuc2)
#---------------------------------------------------
cinsiyet = veriler.iloc[:,-1].values
# .iloc[:,-1] demek son kolonu al demek
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])
#sonuc3 adında verisi cinsiyet,kolon ismi cinsiyet olan 0-21 indislik DataFrame oluşturduk
print(sonuc3)
#---------------------------------------------------
#DataFrame'leri ikişer ikişer birleştiriyoruz
#Step-1
s = pd.concat([sonuc1,sonuc2], axis=1)
print(s)

#Step-2
s2 = pd.concat([s,sonuc3], axis=1)
print(s2)

#sonuç olarak kategorik veriler ile sayısal verileri DataFrame yapısında birleştirdik

