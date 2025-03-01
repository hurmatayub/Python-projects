import streamlit as st
import random
import string
import pyperclip

st.title("🔑 Random Password Generator")


password_length = st.slider("Select Password Length:", min_value=6, max_value=30, value=12)


include_uppercase = st.checkbox("Include Uppercase Letters (A-Z)")
include_numbers = st.checkbox("Include Numbers (0-9)")
include_special_chars = st.checkbox("Include Special Characters (@#$%^&*)")


def generate_password(length, upper, numbers, special):
    characters = string.ascii_lowercase 
    if upper:
        characters += string.ascii_uppercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation

    return "".join(random.choice(characters) for _ in range(length))

if st.button("Generate Password"):
    password = generate_password(password_length, include_uppercase, include_numbers, include_special_chars)
    st.text_input("Generated Password:", password, disabled=True)
    
   
    if st.button("Copy to Clipboard"):
        pyperclip.copy(password)
        st.success("Password copied to clipboard!")

