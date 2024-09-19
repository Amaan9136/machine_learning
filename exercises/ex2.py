# SimpleImputer to impute the missing data

# Importing the necessary libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
file = pd.read_csv('datasets/pima-indians-diabetes.csv')
X=file.iloc[:,:-1].values
y=file.iloc[:,-1].values
# Identify missing data (assumes that missing data is represented as NaN)
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer.fit(X[:,:-1])
X[:,:-1] = imputer.transform(X[:,:-1])
# Print the number of missing entries in each column

# Configure an instance of the SimpleImputer class

# Fit the imputer on the DataFrame

# Apply the transform to the DataFrame

#Print your updated matrix of features
print(X) # matrix 
print(y) # vector