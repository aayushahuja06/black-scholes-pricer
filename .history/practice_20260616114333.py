import numpy as np

# =========================
# Lesson 6: Monte Carlo pricing
# =========================

np.random.seed(42)

spot_price = 100
strike_price = 105
simulations = 10

future_prices = np.random.normal(loc=110, scale=15, size=simulations)
call_payoffs = np.maximum(future_prices - strike_price, 0)
estimated_call_price = call_payoffs.mean()

print("Lesson 6")
print("future prices:", np.round(future_prices, 2))
print("call payoffs:", np.round(call_payoffs, 2))
print("estimated call price:", round(estimated_call_price, 2))


# =========================
# Practice 6
# =========================

# Task 1:
# Make a random seed of 7.
np.random.seed(7)
# Task 2:
# Make a variable named strike and set it equal to 100.
strike = 100
# Task 3:
# Make a variable named simulations and set it equal to 12.
simulations = 12
# Task 4:
# Make a NumPy array named future_prices using np.random.normal
# with loc = 102, scale = 10, size = simulations.
future_prices = np,random.normal(loc = 102, scale = 10, size = simulations)
# Task 5:
# Print future_prices rounded to 2 decimal places.
print(np.round(future_prices, 2))
# Task 6:
# Make a NumPy array named call_payoffs using future_prices and strike.
call_payoffs = np.maximum(future_prices - strike, 0)
# Task 7:
# Print call_payoffs.
print(call_payoffs)
# Task 8:
# Print the average of call_payoffs.
print(np.mean(call_payoffs))
# Task 9:
# Make a NumPy array named put_payoffs using future_prices and strike.
put_payoffs = np.maximum(strike - future_prices, 0)
# Task 10:
# Print put_payoffs.
print(put_payoffs)
# Task 11:
# Print the average of put_payoffs.
print(np.mean(put_payoffs))
# Bonus task:
# Print how many simulated prices finished above strike.
print(np.sum())