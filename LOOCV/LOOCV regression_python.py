# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 13:57:13 2018

@author: Zhao
"""

from scipy import stats
import numpy as np
from sklearn.model_selection import LeaveOneOut

def LOORegression(filepath):
    # loads txt file
    a = np.loadtxt(filepath)  
    Y = np.array(a[0])
    X = np.array(a[1])
    
    # perform Leave-one-out function
    loo = LeaveOneOut()
    loo.get_n_splits(X)
    for train_index, test_index in loo.split(X):
        
        # the indices of data plots used for training and testing during the interation.
        print("TRAIN:", train_index, "TEST:", test_index)
        X_train, X_test = X[train_index], X[test_index]
        Y_train, Y_test = Y[train_index], Y[test_index]
        
        # the number of manual-counted rapeseed leaf of the corresponding plots.
        print(X_train, X_test)
        # the number of manual-counted rapeseed seedlings of the corresponding plots.
        print(Y_train, Y_test)
        
        # Uses the traning data for linear regression
        slope, intercept, r_value, p_value, slope_std_error = stats.linregress(X_train, Y_train)
        
        # Calculates the RMSE based on the traning data
        n = len(X_train)
        sum = 0
        for i in range(n):
            predict_train = slope * X_train[i] + intercept
            di = (Y_train[i] - predict_train)**2
            sum = sum + di
        RMSE = np.math.sqrt(sum/n)
        # RMSE based on training data
        print(RMSE)
        
        # Calculates MAE based on testing data
        Y_predicted = slope * X_test[0] + intercept
        pred_error = abs(Y_test[0] - Y_predicted)
        
        # Joints the formula to display
        if intercept >= 0:
            formula = str(round(slope,3)) + "x+" + str(round(intercept,3))
        else:
            formula = str(round(slope,3)) + "x" + str(round(intercept,3))
            
        # Calculates the r-squared
        r_square = r_value * r_value
        r_squared = round(r_square,3)
        
        # print the result of the interation
        result = [formula, r_squared, round(p_value,3), round(slope_std_error,3), round(Y_predicted,3), round(pred_error,3)]
        print(result)
        print("")
    