import streamlit as st
from src.fibonacci import fibonacci, fibonacci_sequence
from src.utils import math_utils, stats_utils, datetime_utils, finance_utils

st.title("Utilities Service")

CATEGORY_MAP = {
    "Math": math_utils,
    "Statistics": stats_utils,
    "Date/Time": datetime_utils,
    "Finance": finance_utils,
}

category = st.selectbox("Category", list(CATEGORY_MAP.keys()))
module = CATEGORY_MAP[category]

st.subheader(f"{category} utilities")

if category == "Math":
    func = st.selectbox("Function", ["factorial", "gcd", "lcm", "is_prime", "permutations", "combinations"])
    if func == "factorial":
        n = st.number_input("n", min_value=0, value=5, step=1)
        if st.button("Compute"):
            st.write(module.factorial(int(n)))
    elif func in ("gcd", "lcm"):
        a = st.number_input("a", value=12, step=1)
        b = st.number_input("b", value=18, step=1)
        if st.button("Compute"):
            st.write(getattr(module, func)(int(a), int(b)))
    elif func == "is_prime":
        n = st.number_input("n", min_value=0, value=17, step=1)
        if st.button("Check"):
            st.write(module.is_prime(int(n)))
    else:
        n = st.number_input("n", min_value=0, value=5, step=1)
        k = st.number_input("k", min_value=0, value=2, step=1)
        if st.button("Compute"):
            st.write(getattr(module, func)(int(n), int(k)))

elif category == "Statistics":
    func = st.selectbox("Function", ["mean", "median", "mode", "variance", "stdev", "percentiles"])
    raw = st.text_input("Data (comma-separated)", "1,2,3,4,5")
    data = [float(x.strip()) for x in raw.split(",") if x.strip()]
    if func == "percentiles":
        p = st.text_input("Percentiles (comma-separated, 0-100)", "25,50,75")
        ps = [float(x.strip()) for x in p.split(",") if x.strip()]
        if st.button("Compute"):
            st.write(module.percentiles(data, ps))
    else:
        if st.button("Compute"):
            st.write(getattr(module, func)(data))

elif category == "Date/Time":
    func = st.selectbox("Function", ["age", "days_between", "business_days_between"])
    if func == "age":
        bd = st.date_input("Birth date")
        if st.button("Compute"):
            st.write(module.age(bd.isoformat()))
    else:
        s = st.date_input("Start date")
        e = st.date_input("End date")
        if st.button("Compute"):
            st.write(getattr(module, func)(s.isoformat(), e.isoformat()))

elif category == "Finance":
    func = st.selectbox("Function", ["simple_interest", "convert_currency", "loan_amortization"])
    if func == "simple_interest":
        p = st.number_input("Principal", value=1000.0)
        r = st.number_input("Annual rate (decimal)", value=0.05)
        y = st.number_input("Years", value=1)
        if st.button("Compute"):
            st.write(module.simple_interest(p, r, y))
    elif func == "convert_currency":
        amt = st.number_input("Amount", value=100.0)
        rate = st.number_input("Rate", value=1.0)
        if st.button("Convert"):
            st.write(module.convert_currency(amt, rate))
    else:
        principal = st.number_input("Principal", value=10000.0)
        rate = st.number_input("Annual rate (decimal)", value=0.05)
        years = st.number_input("Years", value=1)
        if st.button("Compute schedule"):
            sched = module.loan_amortization(principal, rate, int(years))
            st.write(sched)
