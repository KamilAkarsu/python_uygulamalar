#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:43:07 2018

@author: kamilakarsu
"""

#Eksik Veriler

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

eksikveriler = pd.read_csv('./data/eksikveriler.csv')
#Veri yüklendi

print(eksikveriler)
#Veri ekrana basıldı

#Yas kolonunda eksik veriler tespit edildi
#Missing Value lar yerine herhangi bir değer de atanabilir
#Ama en güzeli missing value lar dısındaki değerlerin ortalamasını kullanmaktır

# sci-kit learn kısaltması sklearn
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy= 'mean',axis=0 )

Yas = eksikveriler.iloc[:,1:4].values
#Pandas kütüphanesinde istenilen satır/sütun seçilmesi için kullanılır
# 1 dahil 4 dahil değil yani satır alma - ve 1,2,3. sütunları al
#1,2,3. sütunları almamızın nedeni imputer'ın sadece sayısal değerlerde
#kullanılıyor olması
print(Yas)

imputer = imputer.fit(Yas[:,1:4])
#.fit ile veri üzerine belirlenen strategy uygulanıyor

Yas[:,1:4] = imputer.transform(Yas[:,1:4])
# .transform veriyi değiştirmek için
print(Yas)


