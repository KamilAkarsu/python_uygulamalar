#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:13:58 2018

@author: kamilakarsu
"""
#Verinin İçeri Alınması (Data Import)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv('./data/veriler.csv')
print(veriler)

boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)

yascinsiyet = veriler[['yas','cinsiyet','boy']]
print(yascinsiyet)

