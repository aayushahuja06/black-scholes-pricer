import pytest
from main import BlackScholes

# test known values
def test_call_price():
    bs = BlackScholes(S=150, K=145, T=0.25, r=0.05, sigma=0.2)
    assert round(bs.call_price(), 2) == 9.86

def test_put_price():
    bs = BlackScholes(S=150, K=145, T=0.25, r=0.05, sigma=0.2)
    assert round(bs.put_price(), 2) == 3.06

# test put-call parity — must always hold
def test_put_call_parity():
    bs = BlackScholes(S=150, K=145, T=0.25, r=0.05, sigma=0.2)
    import numpy as np
    parity = bs.call_price() - bs.put_price()
    expected = bs.S - bs.K * np.exp(-bs.r * bs.T)
    assert round(parity, 4) == round(expected, 4)

# test error handling
def test_negative_volatility():
    with pytest.raises(ValueError):
        BlackScholes(S=150, K=145, T=0.25, r=0.05, sigma=-0.1)

def test_zero_time():
    with pytest.raises(ValueError):
        BlackScholes(S=150, K=145, T=0, r=0.05, sigma=0.2)

def test_negative_stock_price():
    with pytest.raises(ValueError):
        BlackScholes(S=-150, K=145, T=0.25, r=0.05, sigma=0.2)