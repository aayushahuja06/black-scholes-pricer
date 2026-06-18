import numpy as np

# =========================
# Lesson 5: option payoffs
# =========================


# =========================
# Practice 5
# =========================

# Task 1:
# Make a NumPy array named prices with these numbers:
# 80, 90, 100, 110, 120
prices = np.array([80, 90, 100, 110, 120])
# Task 2:
# Make a variable named strike and set it equal to 100.
strike = 100
# Task 3:
# Print the call option payoff for prices using strike.
call_payoff = np.maximum(prices - strike, 0)
# Task 4:
# Print the put option payoff for prices using strike.
put_payoff = np.maximum(strike - prices, 0)
# Task 5:
# Print the average call payoff.
print("Average call payoff:", np.mean(call_payoff))
# Task 6:
# Print the average put payoff.
print("Average put payoff:", np.mean(put_payoff))
# Task 7:
# Make a NumPy array named future_prices using np.random.normal
# with loc = 105, scale = 12, size = 10.
future
# Task 8:
# Print future_prices rounded to 2 decimal places.

# Task 9:
# Print the call payoffs for future_prices using strike.

# Task 10:
# Print the average of the call payoffs from future_prices.

# Bonus task:
# Print how many values in future_prices finish above strike.
