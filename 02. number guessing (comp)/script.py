import streamlit as st
import random

if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
if 'user_guess' not in st.session_state:
    st.session_state.user_guess = None
if 'computer_guess' not in st.session_state:
    st.session_state.computer_guess = None
if 'message' not in st.session_state:
    st.session_state.message = ""
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'computer_attempts' not in st.session_state:
    st.session_state.computer_attempts = 0

st.title("🎯 User vs Computer: Guess the Number")
st.write("Both you and the computer will try to guess the same random number between 1 and 100!")


st.session_state.user_guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

if st.button("Submit Both Guesses"):
    st.session_state.attempts += 1
    st.session_state.computer_attempts += 1
    st.session_state.computer_guess = random.randint(1, 100)
    
    user_message = ""
    computer_message = ""
    
    if st.session_state.user_guess < st.session_state.target_number:
        user_message = "Your guess is too low!"
    elif st.session_state.user_guess > st.session_state.target_number:
        user_message = "Your guess is too high!"
    else:
        user_message = f"🎉 You guessed the number in {st.session_state.attempts} attempts!"
    
    if st.session_state.computer_guess < st.session_state.target_number:
        computer_message = f"Computer guessed {st.session_state.computer_guess}. It's too low!"
    elif st.session_state.computer_guess > st.session_state.target_number:
        computer_message = f"Computer guessed {st.session_state.computer_guess}. It's too high!"
    else:
        computer_message = f"🤖 Computer guessed the number {st.session_state.computer_guess} correctly in {st.session_state.computer_attempts} attempts!"
    
    st.session_state.message = user_message + "\n" + computer_message

st.write(st.session_state.message)

if st.button("Restart Game"):
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.user_guess = None
    st.session_state.computer_guess = None
    st.session_state.message = ""
    st.session_state.attempts = 0
    st.session_state.computer_attempts = 0
    st.write("Game restarted! Try to guess the new number.")
