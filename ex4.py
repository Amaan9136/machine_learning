# Importing the necessary libraries
import pandas
from sklearn.model_selection import train_test_split

# Loading the Iris dataset
file = pandas.read_csv("iris.csv")

# Separate features and target
X=file.iloc[:,:-1].values
y=file.iloc[:,-1].values

# Split the dataset into an 80-20 training-test set
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)

# Printing the matrix of features and the dependent variable vector
print('X_train: ',X_train)
print('X_test: ',X_test)
print('y_train: ',y_train)
print('y_test: ',y_test)
print(X) # matrix 
print(y) # vector


# Apply feature scaling on the training and test sets

# Print the scaled training and test sets