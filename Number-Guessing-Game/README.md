# Project - Number Guessing Game

## Project Overview
The **Number Guessing Game** is a simple Python console game where the computer randomly selects a number between 1 and 100, and the player tries to guess it within a limited number of attempts. The game offers two difficulty levels — Easy and Hard — which determine the number of allowed guesses.

---

## Features
- Random number generation between **1 and 100**.
- **Two difficulty levels**:
  - Easy Mode → 10 attempts
  - Hard Mode → 5 attempts
- Feedback after each guess:
  - "Too HIGH" if the guess is greater than the target number.
  - "Too LOW" if the guess is smaller than the target number.
- Ends the game when the player guesses correctly or runs out of attempts.

---

## How It Works
1. The game starts by asking the player to choose a difficulty level.
2. A random number is generated in the background.
3. The player enters guesses and receives hints to adjust their next guess.
4. The game ends when:
   - The player guesses the correct number.
   - The number of attempts reaches zero.

---

##  How to Run
1. Make sure you have Python installed (version 3.x recommended).
2. Save the script as `number_guessing_game.py`.
3. Open your terminal or command prompt in the project directory.
4. Run the script:
   ```bash
   python number_guessing_game.py

---

## Example Output

## Technologies Used
- Python 3.x  
- Built-in `random` module for number generation.  
- Console/Terminal for user interaction.
