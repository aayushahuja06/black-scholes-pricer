import numpy as np

# =========================
# Lesson 4: random numbers
# =========================

np.random.seed(42)

returns = np.random.normal(loc=0.01, scale=0.02, size=8)

print("Lesson 4")
print("returns:", returns)
print("rounded returns:", np.round(returns, 4))
print("mean return:", returns.mean())
print("max return:", returns.max())
print("min return:", returns.min())

dice = np.random.randint(1, 7, size=10)
print("dice rolls:", dice)


# =========================
# Practice 4
# =========================

# Task 1:
# Make a random seed of 7.
np.random.seed(7)
# Task 2:
# Make a NumPy array named sample using np.random.randint
# with random integers from 1 to 20 and size 8.
sample = np.random.randint(1)
# Task 3:
# Print sample.

# Task 4:
# Print the mean of sample.

# Task 5:
# Print the maximum value in sample.

# Task 6:
# Print the minimum value in sample.

# Task 7:
# Make a NumPy array named noise using np.random.normal
# with loc = 0, scale = 1, size = 6.

# Task 8:
# Print noise.

# Task 9:
# Print noise rounded to 3 decimal places.

# Task 10:
# Print only the values in noise that are greater than 0.

# Bonus task:
# Make a NumPy array named coin_flips using random integers
# that contains 12 values of either 0 or 1, then print it.
