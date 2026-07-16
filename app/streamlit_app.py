import streamlit as st
from src.fibonacci import fibonacci, fibonacci_sequence

st.title("Fibonacci Service")

n = st.number_input("n", min_value=0, value=10, step=1)

if st.button("Compute nth"):
    st.write(f"Fibonacci({n}) = {fibonacci(n)}")

if st.button("Show sequence"):
    st.write(fibonacci_sequence(n))
