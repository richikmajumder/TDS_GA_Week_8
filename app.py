import streamlit as st
st.write("""TDS week 8 Graded Assignment
Build a streamlit web application for the following usecase and host the application using heroku.
UseCase : Division of 2 given numbers . """)
first_number = st.number_input("Enter first number")
second_number = st.number_input("Enter second number")
if second_number == 0:
  st.write("Division by zero not allowed")
  st.write("By Richik Majumder (21f1000460)")
else:
  division = first_number/second_number
  st.write("The division of first_number by second_number is", str(division))
  st.write("By Richik Majumder (21f1000460)")
