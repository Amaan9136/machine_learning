
numbers = list(range(23))
print(numbers)
 
# consider polynomial - n^2 
# consider exponential - 2^n
poly = []

for n in numbers:
 poly.append(pow(n,2))

expo = []

for n in numbers:
 expo.append(pow(2,n))

import matplotlib.pyplot as plt

plt.scatter(numbers,poly,color='red',marker='X')
plt.plot(numbers,poly,color='red',marker='X')
plt.show()

plt.scatter(numbers,expo,color='red',marker='X')
plt.plot(numbers,expo,color='red',marker='X')

plt.show()