import numpy as np

# =========================
# Lesson 7: reusable option pricer
# =========================


def price_call_option(strike, mean_price, std_price, simulations, rate, time):
    future_prices = np.random.normal(loc=mean_price, scale=std_price, size=simulations)
    payoffs = np.maximum(future_prices - strike, 0)
    discount_factor = np.exp(-rate * time)
    option_price = discount_factor * payoffs.mean()
    return future_prices, payoffs, option_price


np.random.seed(42)

future_prices, payoffs, option_price = price_call_option(
    strike=105,
    mean_price=110,
    std_price=15,
    simulations=12,
    rate=0.05,
    time=1,
)

print("Lesson 7")
print("future prices:", np.round(future_prices, 2))
print("payoffs:", np.round(payoffs, 2))
print("estimated option price:", round(option_price, 2))


# =========================
# Practice 7
# =========================

# Task 1:
# Make a random seed of 7.
np.random.seed(7)
# Task 2:
# Make a function named price_put_option with parameters:
# strike, mean_price, std_price, simulations, rate, time
def price_put_option(strike, mean_price, std_price, simulations, rate, time):
    future_prices = np.random.normal(loc=mean_price, scale=std_price, size=simulations)
    put_payoffs = np.maximum(strike - future_prices, 0)
    discount_factor = np.exp(-rate * time)
    discounts_average_payoff = discount_factor * np.mean(put_payoffs)
    return futrue_prices, payoffs, option_price
# Task 3:
# Inside the function, make future_prices using np.random.normal.

# Task 4:
# Inside the function, make put payoffs.

# Task 5:
# Inside the function, make a discount factor using np.exp(-rate * time).

# Task 6:
# Inside the function, make option_price as the discounted average payoff.

# Task 7:
# Return future_prices, payoffs, and option_price from the function.

# Task 8:
# Call price_put_option with:
# strike = 100
# mean_price = 98
# std_price = 12
# simulations = 15
# rate = 0.04
# time = 1

# Task 9:
# Store the returned values in:
# future_prices, payoffs, option_price

# Task 10:
# Print future_prices rounded to 2 decimal places.

# Task 11:
# Print payoffs.

# Task 12:
# Print option_price rounded to 2 decimal places.

# Bonus task:
# Call the function again with simulations = 1000
# and print the new option price rounded to 2 decimal places.
