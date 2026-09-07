import math
from functools import reduce
import numpy as np

# Math functions
num = 16

print("Square root:", math.sqrt(num))
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Log:", math.log(10))

# Reduce function
numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", result)

# NumPy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Mean:", np.mean(a))
print("Sum:", np.sum(b))
