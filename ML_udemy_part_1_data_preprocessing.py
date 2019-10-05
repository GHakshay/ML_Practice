#!/usr/bin/env python
# coding: utf-8

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset=pd.read_csv('Data.csv')
x=dataset.iloc[:,0:3].values #independent variable
y=dataset.iloc[0:, 3].values #dependent variable


# taking care of missing data
from sklearn.preprocessing import Imputer

imputer=Imputer(missing_values="NaN",strategy="mean",axis=0)  #help(Imputer())
imputer=imputer.fit(x[0:,1:3]) # [1:3] upper bound is excluded
x[0:,1:3]=imputer.transform(x[0:,1:3])

# encoding categorical data     OR      making all the data into numerical value for computation
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
label_encoder_x=LabelEncoder()
x[:, 0]=label_encoder_x.fit_transform(x[:, 0]) # this ll create a problem as numerical value is comparable and hence spain>germany>france which is illogical.
#so we ll use "dummy variable" through the class "One hot Encoder"
onehotencoder=OneHotEncoder(categorical_features=[0])
x=onehotencoder.fit_transform(x).toarray()

label_encoder_y=LabelEncoder()
y=label_encoder_y.fit_transform(y)

#splitting dataset into training dataset(to train the machine) and testing dataset(to check the performance)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
X_train=sc_x.fit_transform(X_train)
X_test=sc_x.transform(X_test)


