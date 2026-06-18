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
    
    # internal use only
    def d1(self):
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)
    
    # black-scholes formula for call option price
    def call_price(self):
        call = self.S * norm.cdf(self.d1()) - self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2())
        return call
    # put option price
    def put_price(self):
        put = self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2()) - self.S * norm.cdf(-self.d1())
        return put
    # greeks-----
    # Delta — how much the option price changes when S moves $1
    def delta(self):
        return norm.cdf(self.d1())

    # Gamma — how much delta itself changes when S moves $1
    def gamma(self):
        return norm.pdf(self.d1()) / (self.S * self.sigma * np.sqrt(self.T))

    # Theta — how much the option loses per day as time passes
    def theta(self):
        term1 = -(self.S * norm.pdf(self.d1()) * self.sigma) / (2 * np.sqrt(self.T))
        term2 = self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2())
        return (term1 - term2) / 365

    # Vega — how much the price changes when volatility moves 1%
    def vega(self):
        return self.S * norm.pdf(self.d1()) * np.sqrt(self.T) * 0.01

    # Rho — how much the price changes when interest rates move 1%
    def rho(self):
        return self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(self.d2()) * 0.01



# testing
bs = BlackScholes(S=150, K=145, T=0.25, r=0.05, sigma=0.2)
print(bs.call_price())
print(bs.put_price())
print(bs.delta())
print(bs.gamma())
print(bs.theta())
print(bs.vega())
print(bs.rho())