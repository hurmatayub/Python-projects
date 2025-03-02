# import streamlit as st
# import random
# import string
# import pyperclip

# st.title("Random Password Generator")


# password_length = st.slider("Select Password Length:", min_value=6, max_value=30, value=12)


# include_uppercase = st.checkbox("Include Uppercase Letters (A-Z)")
# include_numbers = st.checkbox("Include Numbers (0-9)")
# include_special_chars = st.checkbox("Include Special Characters (@#$%^&*)")


# def generate_password(length, upper, numbers, special):
#     characters = string.ascii_lowercase 
#     if upper:
#         characters += string.ascii_uppercase
#     if numbers:
#         characters += string.digits
#     if special:
#         characters += string.punctuation

#     return "".join(random.choice(characters) for _ in range(length))

# if st.button("Generate Password"):
#     password = generate_password(password_length, include_uppercase, include_numbers, include_special_chars)
#     st.text_input("Generated Password:", password, disabled=True)
    
   
#     if st.button("Copy to Clipboard"):
#         pyperclip.copy(password)
#         st.success("Password copied to clipboard!")



import streamlit as st
import random
import string

st.title("Random Password Generator")

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
    st.session_state.password = generate_password(password_length, include_uppercase, include_numbers, include_special_chars)

# Display the password if generated
if "password" in st.session_state:
    st.text_input("Generated Password:", st.session_state.password, disabled=True)

    # JavaScript for copying password to clipboard
    st.markdown(
        f"""
        <button onclick="navigator.clipboard.writeText('{st.session_state.password}'); alert('Password copied!');">
            Copy to Clipboard
        </button>
        """,
        unsafe_allow_html=True
    )

