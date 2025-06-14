# -*- coding: utf-8 -*-
"""Regression tree.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13xnI7EqMPAfqjswVQBnJhwioY7Y8eT6c
"""

!pip install numpy
!pip install pandas
!pip install matplotlib
!pip install scikit-learn

# Commented out IPython magic to ensure Python compatibility.
from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings('ignore')

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/pu9kbeSaAtRZ7RxdJKX9_A/yellow-tripdata.csv"
raw_data = pd.read_csv(url)
raw_data

# Optional: ensure all data is numeric before calling .corr()
numeric_data = raw_data.select_dtypes(include=['number'])
correlation_values = numeric_data.corr()['tip_amount'].drop('tip_amount')

correlation_values = raw_data.corr()['tip_amount'].drop('tip_amount')
correlation_values.plot(kind='barh', figsize=(10, 6))

"""we notice that 4 parameters have absolutely no corelation with tip_amount or very less correlation.

Normalisation
"""

y = raw_data[['tip_amount']].values.astype('float32')
proc_data =raw_data.drop(['tip_amount'],axis=1)
x = proc_data.values
x = normalize(x,axis=1,norm ='l1',copy=False)

"""Training and testing"""

x_train,x_test,y_train,y_test =train_test_split(x,y,test_size=0.2,random_state=42)

"""Build a decision tree"""

!pip install -U scikit-learn

# import the Decision Tree Regression Model from scikit-learn
from sklearn.tree import DecisionTreeRegressor

# for reproducible output across multiple function calls, set random_state to a given integer value
dt_reg = DecisionTreeRegressor(criterion = 'squared_error',
                               max_depth=8,
                               random_state=35)

dt_reg.fit(x_train,y_train)

"""evaluation"""

y_pred =dt_reg.predict(x_test)
mse_score = mean_squared_error(y_test,y_pred)
print('mse:{0:3f}'.format(mse_score))
r2_score =dt_reg.score(x_test,y_test)
print('r2_score:{0:3f}'.format(r2_score))