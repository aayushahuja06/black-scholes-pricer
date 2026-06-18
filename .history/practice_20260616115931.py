import numpy as np

# =========================
# Final Challenge
# =========================

# Task 1:
# Make a random seed of 7.
np.random.seed(7)
# Task 2:
# Make a function named simulate_prices with parameters:
# mean_price, std_price, simulations
def simulate_prices(mean_price, std_price, simulations):
    return std_price * np.random.normal(size=simulations) + mean_price
# Task 3:
# Inside simulate_prices, return simulated prices using np.random.normal.

# Task 4:
# Make a function named price_call_option with parameters:
# future_prices, strike, rate, time
def price_call_option(future_prices, strike, rate, time):
    call_payoffs = np.maximum(future_prices - strike, 0)
    discounted_call_price = np.exp(-rate * time) * np.mean(call_payoffs)
    return discounted_call_price
# Task 5:
# Inside price_call_option, make call payoffs and return the discounted option price.
def price_call_option(future_prices, strike, rate, time):
    call_payoffs = np.maximum(future_prices - strike, 0)
    discounted_call_price = np.exp(-rate * time) * np.mean(call_payoffs)
    return discounted_call_price
# Task 6:
# Make a function named price_put_option with parameters:
# future_prices, strike, rate, time

# Task 7:
# Inside price_put_option, make put payoffs and return the discounted option price.

# Task 8:
# Make these variables:
# strike = 100
# mean_price = 103
# std_price = 14
# simulations = 5000
# rate = 0.05
# time = 1

# Task 9:
# Make future_prices by calling simulate_prices.

# Task 10:
# Make call_price by calling price_call_option.

# Task 11:
# Make put_price by calling price_put_option.

# Task 12:
# Print the average of future_prices rounded to 2 decimal places.

# Task 13:
# Print call_price rounded to 2 decimal places.

# Task 14:
# Print put_price rounded to 2 decimal places.

# Task 15:
# Print how many simulated prices finished above strike.

# Bonus task:
# Change strike to 110 and print the new call price and put price rounded to 2 decimal places.
