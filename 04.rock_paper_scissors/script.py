import streamlit as st
import random

def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

st.title("Rock Paper Scissors Game")

options = ["Rock", "Paper", "Scissors"]

user_choice = st.selectbox("Choose your move:", options)


computer_choice = st.selectbox("Computer chooses:", options, index=random.randint(0, 2))

if st.button("Play!"):
    result = get_winner(user_choice, computer_choice)
    st.write(f"**Your choice:** {user_choice}")
    st.write(f"**Computer's choice:** {computer_choice}")
    st.subheader(result)
