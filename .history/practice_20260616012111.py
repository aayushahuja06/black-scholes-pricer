import numpy as np

# =========================
# Lesson 3: boolean filtering
# =========================

temps = np.array([72, 68, 75, 81, 64, 79, 85])

print("Lesson 3")
print("temps:", temps)
print("temps > 75:", temps > 75)
print("hot temps:", temps[temps > 75])
print("temps <= 70:", temps <= 70)
print("cool temps:", temps[temps <= 70])
print("between 70 and 80:", temps[(temps >= 70) & (temps <= 80)])


# =========================
# Practice 3
# =========================

# Task 1:
# Make a NumPy array named prices with these numbers:
# 95, 102, 88, 120, 110, 79, 130
prices = np.array([95, 102, 88, 120, 110, 79, 130])
# Task 2:
# Print a boolean array showing which values in prices are greater than 100.
print("prices > 100:", prices > 100)
# Task 3:
# Print only the values in prices that are greater than 100.
print("prices > 100:", prices[prices > 100])
# Task 4:
# Print a boolean array showing which values in prices are less than 90.
print("prices < 90:", prices < 90)
# Task 5:
# Print only the values in prices that are less than 90.
print("prices < 90:", prices[prices < 90])
# Task 6:
# Print only the values in prices that are between 90 and 120 inclusive.
print("prices < 90:", prices[prices >= 90] )
# Task 7:
# Print how many values in prices are greater than 100.

# Task 8:
# Print how many values in prices are less than 90.

# Task 9:
# Make a NumPy array named changes with these numbers:
# -2, 5, 0, -1, 3, 7, -4

# Task 10:
# Print only the positive values from changes.

# Task 11:
# Print only the negative values from changes.

# Bonus task:
# Print only the values in changes that are not zero.
