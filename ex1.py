# Importing the necessary libraries
import pandas
from sklearn.model_selection import train_test_split

# Loading the Iris dataset
file = pandas.read_csv("iris.csv")

# Creating the matrix of features (X) and the dependent variable vector (y)
X=file.iloc[:,:-1].values
y=file.iloc[:,-1].values


xtrain,xtest,ytrain,ytest = train_test_split(X,y)

# Printing the matrix of features and the dependent variable vector
print(xtrain)
print(xtest)
print(ytrain)
print(ytest)
print(X) # matrix 
print(y) # vector