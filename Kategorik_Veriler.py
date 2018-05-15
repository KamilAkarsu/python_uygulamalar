#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:12:51 2018

@author: kamilakarsu
"""
#Kategorik Veriler

import pandas as pd

veriler = pd.read_csv('./data/veriler.csv')

ulke = veriler.iloc[:,0:1].values
#0.kolonu al
print(ulke)

#---------------------------------------------------
from sklearn.preprocessing import LabelEncoder
#LabelEncoder encoder ını import et
#birebir verilen labelleri-değerleri sayıya çevirir

le = LabelEncoder()
#labelencoder nesnesi oluştur

ulke[:,0] = le.fit_transform(ulke[:,0])
#fit_transform -> uygula ve sonucu değiştir
print(ulke)

#---------------------------------------------------
from sklearn.preprocessing import OneHotEncoder
#OneHotEncoder encoder ını import et
#kolon bazlı olarak kolon başlığına çevirir her bir etiketi
#o kolon başlığı altında ise 1 değilse 0 koyarak ilerler

ohe = OneHotEncoder()
#onehotencoder nesnesi oluştur

ulke = ohe.fit_transform(ulke).toarray()
#ulke veri yapısına dizi olarak ohe yi uygula ve sonucu değiştir
print(ulke)
