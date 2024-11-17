'''Performing binning based on predictive value in Python involves dividing a continuous variable into discrete intervals (or "bins") based on a model predicted outcomes. This is useful for improving the interpretability of your model, and in some cases, it can help with feature engineering by reducing the complexity of continuous variables. There are different strategies to perform binning, but here we will focus on two main approaches:

Equal-width binning: The range of values is divided into equal-width bins.
Quantile binning: The data is divided into bins such that each bin contains an equal number of data points.
Binning based on model predictions: Binning the continuous feature values based on predicted probabilities or outcomes from a predictive model.'''

#Example 1: Binning Based on Predicted Probabilities 
'Let’s use a logistic regression model for classification and create bins based on predicted probabilities. This is useful when you want to discretize the predicted probabilities into classes.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification

# Generate a synthetic classification dataset
X, y = make_classification(n_samples=1000, n_features=5, random_state=42)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict probabilities on the test set
y_prob = model.predict_proba(X_test)[:, 1]  # Predicted probabilities for the positive class

# Perform binning based on predicted probabilities
# Define bins based on quantiles or equal-width (you can choose the method)
bins = [0, 0.3, 0.6, 1.0]  # These are arbitrary thresholds for binning
labels = ['Low', 'Medium', 'High']  # Bin labels

# Bin the predicted probabilities
binned_predictions = pd.cut(y_prob, bins=bins, labels=labels, include_lowest=True)

# Add binned predictions to the DataFrame
df = pd.DataFrame({'Predicted Probabilities': y_prob, 'Binned Predictions': binned_predictions})

# Display the first few rows
print(df.head())

'''output:
Predicted Probabilities Binned Predictions
0                    0.68             Medium
1                    0.94              High
2                    0.12               Low
3                    0.58             Medium
4                    0.09               Low '''

#Example 2: Binning Based on Predicted Values (Regression)
'If you are using a regression model, you may want to bin the predicted continuous values into discrete intervals. For example, if you are predicting house prices or salaries, you could categorize the predictions into price ranges.

from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generate a synthetic regression dataset
X, y = make_regression(n_samples=1000, n_features=5, noise=0.1, random_state=42)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train a linear regression model
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

# Predict continuous values on the test set
y_pred = reg_model.predict(X_test)

# Perform binning based on predicted values
# For example, binning predicted values into three categories: Low, Medium, High
bins = [-np.inf, -100, 0, 100, np.inf]  # Set custom bin edges
labels = ['Very Low', 'Low', 'High', 'Very High']  # Bin labels

# Bin the predicted values
binned_predictions = pd.cut(y_pred, bins=bins, labels=labels)

# Add binned predictions to the DataFrame
df = pd.DataFrame({'Predicted Values': y_pred, 'Binned Predictions': binned_predictions})

# Display the first few rows
print(df.head())

from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generate a synthetic regression dataset
X, y = make_regression(n_samples=1000, n_features=5, noise=0.1, random_state=42)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train a linear regression model
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

# Predict continuous values on the test set
y_pred = reg_model.predict(X_test)

# Perform binning based on predicted values
# For example, binning predicted values into three categories: Low, Medium, High
bins = [-np.inf, -100, 0, 100, np.inf]  # Set custom bin edges
labels = ['Very Low', 'Low', 'High', 'Very High']  # Bin labels

# Bin the predicted values
binned_predictions = pd.cut(y_pred, bins=bins, labels=labels)

# Add binned predictions to the DataFrame
df = pd.DataFrame({'Predicted Values': y_pred, 'Binned Predictions': binned_predictions})

# Display the first few rows
print(df.head())

from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

# Generate a synthetic regression dataset
X, y = make_regression(n_samples=1000, n_features=5, noise=0.1, random_state=42)

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train a linear regression model
reg_model = LinearRegression()
reg_model.fit(X_train, y_train)

# Predict continuous values on the test set
y_pred = reg_model.predict(X_test)

# Perform binning based on predicted values
# For example, binning predicted values into three categories: Low, Medium, High
bins = [-np.inf, -100, 0, 100, np.inf]  # Set custom bin edges
labels = ['Very Low', 'Low', 'High', 'Very High']  # Bin labels

# Bin the predicted values
binned_predictions = pd.cut(y_pred, bins=bins, labels=labels)

# Add binned predictions to the DataFrame
df = pd.DataFrame({'Predicted Values': y_pred, 'Binned Predictions': binned_predictions})

# Display the first few rows
print(df.head())

'''output:
Predicted Values Binned Predictions
0         -96.43250           Very Low
1         139.17843               High
2          -1.23123                Low
3          67.74126               High
4          89.30321               High '''



