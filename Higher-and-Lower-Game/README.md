# Project - Higher or Lower Game

## Project Overview
The **Higher or Lower Game** is a Python console-based game where the player compares two famous personalities, brands, or organizations based on their follower counts. The player must guess which one has more followers. The game continues until the player makes a wrong guess, and the final score is displayed at the end.

---

## Features
- **Randomized choices** from a predefined dataset of celebrities, brands, and organizations.
- Displays **name, description, and country** for each choice.
- **Interactive gameplay**:
  - Guess whether "A" or "B" has more followers.
  - Score increases for every correct guess.
- Game continues until the first wrong guess.
- Final score displayed at the end.

---

## How It Works
1. At the start of the game, a random choice (Choice A) is selected from the dataset.
2. Another random choice (Choice B) is selected for comparison.
3. The player guesses whether A or B has more followers.
4. If correct:
   - Score increases by 1.
   - Choice B becomes the new Choice A.
   - A new Choice B is generated.
5. If incorrect:
   - The game ends.
   - The final score is displayed.

---

## How to Run
1. Make sure Python is installed (version 3.x recommended).
2. Ensure both `higher_lower_game.py` and `game_data.py` are in the same directory.
3. Open a terminal or command prompt in that directory.
4. Run the game:
   ```bash
   python higher_lower_game.py

---

## Example Output
<img width="1101" height="466" alt="Image" src="https://github.com/user-attachments/assets/de4b1df9-adea-4405-8181-612f5dcca70b" />

---

## Technologies Used
- Python 3.x
- random module for generating random choices
- os module for clearing the console
- Custom Python module (game_data.py) for storing ASCII art and dataset
