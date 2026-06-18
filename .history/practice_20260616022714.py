import numpy as np

# =========================
# Lesson 5: option payoffs
# =========================

stock_prices = np.array([90, 95, 100, 105, 110, 115])
strike_price = 100

call_payoff = np.maximum(stock_prices - strike_price, 0)
put_payoff = np.maximum(strike_price - stock_prices, 0)

print("Lesson 5")
print("stock prices:", stock_prices)
print("call payoff:", call_payoff)
print("put payoff:", put_payoff)
print("average call payoff:", call_payoff.mean())
print("average put payoff:", put_payoff.mean())


# =========================
# Practice 5
# =========================

# Task 1:
# Make a NumPy array named prices with these numbers:
# 80, 90, 100, 110, 120
prices = np.array([80, 90, 100, 110, 120])
# Task 2:
# Make a variable named strike and set it equal to 100.
strik
# Task 3:
# Print the call option payoff for prices using strike.

# Task 4:
# Print the put option payoff for prices using strike.

# Task 5:
# Print the average call payoff.

# Task 6:
# Print the average put payoff.

# Task 7:
# Make a NumPy array named future_prices using np.random.normal
# with loc = 105, scale = 12, size = 10.

# Task 8:
# Print future_prices rounded to 2 decimal places.

# Task 9:
# Print the call payoffs for future_prices using strike.

# Task 10:
# Print the average of the call payoffs from future_prices.

# Bonus task:
# Print how many values in future_prices finish above strike.
