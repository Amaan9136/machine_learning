# Encoder : Text to number conventions using ColumnTransformer (X-independent ), LabelEncoder (y-dependent)

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Load the dataset
data = pd.read_csv('titanic.csv')

# Identify categorical features
categorical_features = ['Name', 'Sex', 'Ticket', 'Cabin']

# Encode categorical features with OneHotEncoder
encoder = OneHotEncoder() 
transformer = ColumnTransformer(transformers=[('encoder', encoder, categorical_features)]) 
X = transformer.fit_transform(data.iloc[:, :-1])

# Encode Embarked with LabelEncoder
le = LabelEncoder()
y = le.fit_transform(data['Survived'])  # Encode target variable - Dependent

# Print the transformed features and encoded target
print(X) # matrix 
print(y) # vector
