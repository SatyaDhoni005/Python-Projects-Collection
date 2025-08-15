# Project - Rock Paper Scissors Game (Tkinter)

## Project Overview
The **Rock Paper Scissors Game** is a simple GUI-based Python project built using Tkinter.  
The player competes against the computer by choosing **Rock**, **Paper**, or **Scissors**.  
The game displays both the player’s and computer’s choices using images, keeps track of scores, and declares the winner after each round.

---

## Features
- Graphical User Interface (GUI) built with **Tkinter**.
- Displays images for both **user** and **computer** choices.
- Tracks and displays scores for both players.
- Randomized computer choices for fair gameplay.
- Instant feedback messages after each round:
  - "You Win"
  - "You Lose"
  - "It's a Tie!"

---

## How It Works
1. The player clicks one of the three buttons: **ROCK**, **PAPER**, or **SCISSOR**.
2. The computer randomly selects a choice.
3. Both choices are displayed using images.
4. The game logic decides the winner:
   - Rock beats Scissor
   - Scissor beats Paper
   - Paper beats Rock
5. Scores are updated accordingly.
6. The game continues until the player decides to close the window.

---

## How to Run
1. Make sure you have Python installed (version 3.x recommended).
2. Install the Pillow library for image handling:
   ```bash
   pip install pillow
3. Place all game image files in the same directory as the script:
    - rock-user.png
    - paper-user.png
    - scissors-user.png
    - rock.png
    - paper.png
    - scissors.png
4. Save the script as Rock_Paper_Scissors.py.

5. Run the script:
   ```bash
   python Rock_Paper_Scissors.py

---

## Example Output
<img width="1916" height="1011" alt="Image" src="https://github.com/user-attachments/assets/cca89998-4056-48c5-a01e-a628dcf92509" />

---

## Technologies Used
- Python 3.x
- Tkinter (for GUI development)
- Pillow (PIL) for image handling
- random module for generating computer choices
