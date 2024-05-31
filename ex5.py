# Feature Scaling - Standardization

# Import necessary libraries
import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the Wine Quality Red dataset
file = pandas.read_csv("winequality-red.csv", delimiter=';')

# Separate features and target
X=file.iloc[:,:-1].values
y=file.iloc[:,-1].values
# Split the dataset into an 80-20 training-test set
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)
# Create an instance of the StandardScaler class
ss = StandardScaler()

# Fit the StandardScaler on the features from the training set and transform it
X_train=ss.fit_transform(X_train)

'''
use transform only, since using fit once is enough 
else it will re calculate standard deviation for all the data which is dangerous
so use like this:

fit: to apply formulas (mean & standard deviation)
transform: to apply changes 

for each variable X & y you need to apply again but no need for similar variables... 

fit / fit_transform
transform
transform....

NOTE: NEED TO APPLY FIT AND TRANSFORM SEPARATELY FOR TEST AND TRAIN SETS.
SO SPLIT THE DATA FIRST 
THEN APPLY FEATURE SCALING
'''

# Apply the transform to the test set
X_test=ss.transform(X_test)

# Print the scaled training and test datasets
print(X_train)
print(X_test)