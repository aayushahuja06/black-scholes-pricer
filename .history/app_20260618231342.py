import streamlit as st
from main import BlackScholes

st.title("Black-Scholes Options Pricer")

st.sidebar.header("Inputs")
S = st.sidebar.slider("Stock price (S)", 50.0, 300.0, 150.0)
K = st.sidebar.slider("Strike price (K)", 50.0, 300.0, 145.0)
T = st.sidebar.slider("Time to expiry (T) in years", 0.01, 2.0, 0.25)
r = st.sidebar.slider("Risk-free rate (r)", 0.0, 0.2, 0.05)
sigma = st.sidebar.slider("Volatility (σ)", 0.01, 1.0, 0.2)

bs = BlackScholes(S=S, K=K, T=T, r=r, sigma=sigma)

st.subheader("Option Prices")
col1, col2 = st.columns(2)
col1.metric("Call Price", f"${bs.call_price():.2f}")
col2.metric("Put Price", f"${bs.put_price():.2f}")

st.subheader("Greeks")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Delta", f"{bs.delta():.4f}")
col2.metric("Gamma", f"{bs.gamma():.4f}")
col3.metric("Theta", f"{bs.theta():.4f}")
col4.metric("Vega", f"{bs.vega():.4f}")
col5.metric("Rho", f"{bs.rho():.4f}")

st.subheader("Implied Volatility")
market_price = st.number_input("Enter market price of call option", value=9.86)
iv = bs.implied_volatility(market_price)
st.metric("Implied Volatility", f"{iv:.2%}")