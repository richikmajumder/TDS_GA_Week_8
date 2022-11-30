import streamlit as st
st.write("""TDS week 8 Graded Assignment""")
st.write("""Streamlit web application for division of 2 given numbers""")
first_number = st.number_input("Enter first number")
second_number = st.number_input("Enter second number")
if second_number == 0:
  st.write("Division by zero not allowed")
  st.write("By Richik Majumder (21f1000460)")
else:
  division = first_number/second_number
  st.write("Answer is", str(division))
  st.write("By Richik Majumder (21f1000460)")
