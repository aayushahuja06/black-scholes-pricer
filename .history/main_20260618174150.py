import numpy as np
from scipy.stats import norm

# Using a class instead of standalone functions so we can store the 5 inputs
# once and call price(), delta(), gamma() etc. without re-passing them each time

class BlackScholes:
    def __init__(self, S, K, T, r, sigma):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma