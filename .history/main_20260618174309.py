import numpy as np
from scipy.stats import norm

# A class lets us encapsulate a single option contract — set the inputs once,
# then expose price and Greeks as methods. Keeps the interface clean and mirrors
# how a real pricing library would be structured.

class BlackScholes:
    def __init__(self, S, K, T, r, sigma):
        self.S = S        # current stock price
        self.K = K        # strike price
        self.T = T        # time to expiry in years
        self.r = r        # risk-free rate (e.g. 0.05 for 5%)
        self.sigma = sigma  # annualized volatility (e.g. 0.2 for 20%)