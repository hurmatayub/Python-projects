import streamlit as st
import random


if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'guess' not in st.session_state:
    st.session_state.guess = None
if 'message' not in st.session_state:
    st.session_state.message = ""

st.title("Number Guessing Game")
st.write("Guess a number between 1 and 100!")

user_input = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.guess = user_input
    if st.session_state.guess < st.session_state.target_number:
        st.session_state.message = "Too low! Try again."
    elif st.session_state.guess > st.session_state.target_number:
        st.session_state.message = "Too high! Try again."
    else:
        st.session_state.message = "🎉 Congratulations! You guessed the correct number!"
        st.session_state.target_number = random.randint(1, 100) 

st.write(st.session_state.message)

if st.button("Restart Game"):
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.guess = None
    st.session_state.message = ""
    st.write("Game restarted! Guess a new number.")
