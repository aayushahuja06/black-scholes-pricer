import numpy as np
from scipy.stats import norm

# Class lets us set inputs once and call price/Greeks as methods

class BlackScholes:
    def __init__(self, S, K, T, r, sigma):
        self.S = S        # current stock price
        self.K = K        # strike
        self.T = T        # time to expiry
        self.r = r        # risk-free rate
        self.sigma = sigma  # annualized volatility
    
    #internal use onyl
    def d1(self):
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)
    
    #black-scholes formula for call option price
    def price(self):
        call = self.S * norm.cdf(self.d1()) - self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2())
        return call
    
    def delta(self):
        
        return norm.cdf(self._d1())
    
#testing
bs = BlackScholes(S=150, K=145, T=0.25, r=0.05, sigma=0.2)
print(bs.price())
print(bs.delta())