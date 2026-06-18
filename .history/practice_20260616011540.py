import numpy as np

# =========================
# Lesson 2: indexing and slicing
# =========================

grid = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nLesson 2")
print(grid)
print(grid[0, 0])
print(grid[2, 2])
print(grid[0])
print(grid[:, 1])
print(grid[:2, :2])


# =========================
# Practice 2
# =========================

# Task 1:
# Make a NumPy array named d with these numbers:
# 5, 10, 15, 20, 25, 30
d = np.array([5, 10, 15, 20, 25, 30])
# Task 2:
# Print the first value in d.
print(d[0])
# Task 3:
# Print the last value in d.
print(d[-1])
# Task 4:
# Print the first 4 values in d.
print(d[:4])
# Task 5:
# Print every second value in d.
print(d[::2])
# Task 6:
# Make a 3x3 NumPy array named e with these rows:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
e = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Task 7:
# Print the middle value from e.
print(e[1,1])
# Task 8:
# Print the second row from e.
print(e[1])
# Task 9:
# Print the third column from e.
print(e[:,2])
# Task 10:
# Print the bottom-right 2x2 section of e.
printe[e(1,1)]
# Bonus task:
# Print the values from d in reverse order.
