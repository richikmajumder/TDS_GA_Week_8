import streamlit as st
st.write("""TDS week 8 Graded Assignment
Build a streamlit web application for the following usecase and host the application using heroku.
UseCase : Division of 2 given numbers . """)
first_no = st.number_input("Enter first number")
second_no = st.number_input("Enter second number")
if second_no == 0:
  st.write("Division by zero not allowed")
else:
  division = first_no/second_no
  st.write("The product of given numbers is", str(division))
  st.write("By Richik Majumder (21f1000460)")
