import streamlit as st
import random


words = ['python', 'streamlit', 'programming', 'developer', 'hangman', 'coding', 'project']


if 'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guesses = []
    st.session_state.attempts = 6

word = st.session_state.word
hidden_word = ''.join([letter if letter in st.session_state.guesses else '_' for letter in word])

st.title("Hangman Game")
st.subheader("Guess the word letter by letter!")

st.write(f"Word: {hidden_word}")
st.write(f"Attempts left: {st.session_state.attempts}")
st.write(f"Guessed letters: {', '.join(st.session_state.guesses) if st.session_state.guesses else 'None'}")


guess = st.text_input("Enter a letter:", max_chars=1).lower()

if st.button("Submit Guess") and guess:
    if guess in st.session_state.guesses:
        st.warning("You've already guessed that letter!")
    elif guess in word:
        st.session_state.guesses.append(guess)
        st.success("Correct guess!")
    else:
        st.session_state.guesses.append(guess)
        st.session_state.attempts -= 1
        st.error("Wrong guess!")

    
    if set(word) <= set(st.session_state.guesses):
        st.success(f" Congratulations! You guessed the word: {word}")
        if st.button("Play Again"):
            st.session_state.word = random.choice(words)
            st.session_state.guesses = []
            st.session_state.attempts = 6
            st.rerun()
    elif st.session_state.attempts == 0:
        st.error(f"Game Over! The correct word was: {word}")
        if st.button("Try Again"):
            st.session_state.word = random.choice(words)
            st.session_state.guesses = []
            st.session_state.attempts = 6
            st.rerun()
