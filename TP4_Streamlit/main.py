import streamlit as st
import pandas as pd
import math

st.title("Mortgage Repayments Calculator")

st.write("### Input Data")

col1, col2 = st.columns(2)

home_value = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (%)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (years)", min_value=1, value=30)

loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12

if monthly_interest_rate > 0:
    monthly_payment = (
        loan_amount
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
        / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    )
else:
    monthly_payment = loan_amount / number_of_payments

total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### Repayments")

col1, col2, col3 = st.columns(3)

col1.metric("Monthly Payment", f"${monthly_payment:,.2f}")
col2.metric("Total Payments", f"${total_payments:,.0f}")
col3.metric("Total Interest", f"${total_interest:,.0f}")

# Payment schedule
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)

    schedule.append([year, remaining_balance])

df = pd.DataFrame(schedule, columns=["Year", "Remaining Balance"])
payments_df = df.groupby("Year").min()

st.write("### Payment Schedule")
st.line_chart(payments_df)