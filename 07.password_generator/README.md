# Random Password Generator

This is a **Random Password Generator** built with **Streamlit**. It allows users to generate strong, random passwords with customizable options like uppercase letters, numbers, and special characters.

##  Features

- Select password length (6-30 characters)
- Include uppercase letters (A-Z)
- Include numbers (0-9)
- Include special characters (@#\$%^&\*)
- Password generated dynamically
- One-click copy to clipboard functionality

##  Live Demo

[Try it here](https://password-generator-by-hurmat-ayub.streamlit.app/)

##  Code Overview

- `app.py`: Main application file that contains the logic for generating passwords and the Streamlit UI.
- Uses **Python’s ****************************`random`**************************** and ****************************`string`**************************** modules** to generate secure passwords.
- Stores the generated password in `st.session_state` to prevent loss on UI updates.
- JavaScript button for copying password to clipboard.

##  How It Works

1. Adjust the slider to set the desired password length.
2. Check/uncheck options to customize your password.
3. Click the **Generate Password** button.
4. Copy the generated password using the **Copy to Clipboard** button.



##  Author

Developed by **Hurmat Muhammad Ayub.**

