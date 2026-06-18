import numpy as np
from scipy.stats import norm



class BlackScholes:
    def __init__(self, S, K, T, r, sigma):
        self.S = S        # current stock price
        self.K = K        # strike
        self.T = T        # time to expiry
        self.r = r        # risk-free rate
        self.sigma = sigma  # annualized volatility