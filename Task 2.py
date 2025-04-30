import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson
#Required Libraries
#streamlit
#numpy
#matplotlib
#scipy

st.set_page_config(page_title="Distribution Visualizer", layout="wide")
st.title("Interactive Probability Distribution Visualizer")

# Sidebar for distribution selection
dist = st.sidebar.selectbox("Choose Distribution", ["Normal", "Binomial", "Poisson"])

fig, ax = plt.subplots(figsize=(8, 4))

if dist == "Normal":
    mu = st.sidebar.slider("Mean (μ)", -5.0, 5.0, 0.0, 0.1)
    sigma = st.sidebar.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0, 0.1)
    show_cdf = st.sidebar.checkbox("Show CDF", False)
    
    x = np.linspace(-10, 10, 1000)  # Fixed x-range for consistent scale
    pdf = norm.pdf(x, mu, sigma)
    cdf = norm.cdf(x, mu, sigma)
    
    ax.plot(x, pdf, label="PDF", color="blue")
    if show_cdf:
        ax.plot(x, cdf, label="CDF", color="green", linestyle="--")
    ax.set_ylim(0, 0.45)  # Fixed y-scale for normal distribution
    ax.set_title(f"Normal Distribution N({mu}, {sigma}²)")
    ax.set_xlabel("x")
    ax.set_ylabel("Density / Probability")
    ax.legend()
    ax.grid(True)

elif dist == "Binomial":
    n = st.sidebar.slider("Number of trials (n)", 1, 50, 10)
    p = st.sidebar.slider("Success probability (p)", 0.0, 1.0, 0.5, 0.01)
    show_cdf = st.sidebar.checkbox("Show CDF", False)
    
    x = np.arange(0, n+1)
    pmf = binom.pmf(x, n, p)
    cdf = binom.cdf(x, n, p)
    
    # Use line plot for PMF
    ax.plot(x, pmf, marker='o', label="PMF", color="blue")
    if show_cdf:
        ax.plot(x, cdf, marker='x', label="CDF", color="green", linestyle="--")
    ax.set_ylim(0, 1.05)  # Fixed y-scale for binomial
    ax.set_title(f"Binomial Distribution B(n={n}, p={p})")
    ax.set_xlabel("Number of Successes")
    ax.set_ylabel("Probability")
    ax.legend()
    ax.grid(True)

elif dist == "Poisson":
    lam = st.sidebar.slider("Lambda (λ)", 0.1, 20.0, 5.0, 0.1)
    show_cdf = st.sidebar.checkbox("Show CDF", False)
    
    x = np.arange(0, 40)
    pmf = poisson.pmf(x, lam)
    cdf = poisson.cdf(x, lam)
    
    # Use line plot for PMF
    ax.plot(x, pmf, marker='o', label="PMF", color="blue")
    if show_cdf:
        ax.plot(x, cdf, marker='x', label="CDF", color="green", linestyle="--")
    ax.set_ylim(0, 0.45)  # Fixed y-scale for Poisson
    ax.set_title(f"Poisson Distribution λ={lam}")
    ax.set_xlabel("Number of Events")
    ax.set_ylabel("Probability")
    ax.legend()
    ax.grid(True)

st.pyplot(fig)
