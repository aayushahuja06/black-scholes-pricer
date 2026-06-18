import numpy as np

# Lesson 1: basic NumPy arrays

# =========================
# Practice
# =========================

# Task 1:
# Make a NumPy array named b with these numbers: 10, 20, 30, 40, 50
# Then print b.
b = np.array([10, 20, 30, 40, 50])
print(b)
# Task 2:
# Print b * 3
# This should multiply every number in b by 3.
print(b*3)
# Task 3:
# Print b + 7
# This should add 7 to every number in b.

# Task 4:
# Print the mean of b.
print(np.mean(b))
# Task 5:
# Print the shape of b.
print(b.shape)
# Task 6:
# Print only the first 3 values from b.

print(b[:3])
# Task 7:
# Make a 2D NumPy array named c like this:
# [[1, 2, 3],
#  [4, 5, 6]]
# Then print c and print its shape.
c =np.array([[1,2,3], [4,5,6]])
print(c)
print(c.shape)
# Bonus task:
# Make an array called prices with 5 stock prices.
# Then print:
# 1. the average price
# 2. the highest price
# 3. the lowest price
