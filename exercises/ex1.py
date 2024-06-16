# Splitting (X-independent ) & (y-dependent) variables

# Importing the necessary libraries
import pandas

# Loading the Iris dataset
file = pandas.read_csv("datasets/iris.csv")


# Creating the matrix of features (X) and the dependent variable vector (y)
X=file.iloc[:,:-1].values
y=file.iloc[:,-1].values

print(X) # matrix 
print(y) # vector