# Hangman Game

This is a **Hangman** game built using **Streamlit** in Python. Players try to guess a randomly selected word by guessing one letter at a time. The game tracks the number of incorrect attempts and ends when the player either guesses the word correctly or runs out of attempts.

## Live Demo
Play the game online: [Hangman Game](https://hangman-by-hurmat-ayub.streamlit.app/)

## Features
- Interactive UI using Streamlit
- Random word selection from a predefined list
- Tracks guessed letters and remaining attempts
- Displays feedback for correct and incorrect guesses
- Option to restart the game after winning or losing

## Installation
To run this project locally, follow these steps:

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/hangman-streamlit.git
   cd hangman-streamlit
   ```
2. Install the required dependencies:
   ```sh
   pip install streamlit
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## How to Play
1. A random word is chosen, and its letters are hidden.
2. Enter a letter in the input box and click **Submit Guess**.
3. If the letter is in the word, it is revealed.
4. If the letter is incorrect, you lose an attempt.
5. The game ends when you either guess the word or run out of attempts.
6. You can restart the game by clicking **Play Again** or **Try Again**.

## Game Rules
- You have **6 attempts** to guess the word.
- Correct guesses reveal letters in the word.
- Incorrect guesses reduce the number of attempts.
- The game is won if all letters are guessed before attempts run out.

## Technologies Used
- **Python**
- **Streamlit**
- **Random module**

## Author
**Hurmat Muhammad Ayub**

Enjoy playing Hangman! 😊

