# Project - True or False Quiz Game

## Project Overview
The **True or False Quiz Game** is a simple Python console application that tests the player's general knowledge with a series of true or false questions. The player is shown one question at a time and must answer with "True" or "False". At the end of the quiz, the final score is displayed.

---

## Features
- **Predefined set of questions** stored in a Python list.
- **Question and Answer system** using a custom `Question` class.
- Immediate feedback after each question:
  - Informs whether the answer was correct or wrong.
  - Displays the current score after every question.
- Game automatically ends when all questions are answered.
- Final score shown at the end of the quiz.

---

## How It Works
1. The game stores all questions and answers in a data list.
2. Each question is converted into a `Question` object containing:
   - The question text.
   - The correct answer.
3. The `QuizBrain` class:
   - Keeps track of the current question number.
   - Checks the player’s answer against the correct answer.
   - Updates and displays the score after each question.
4. The quiz continues until there are no more questions left.
5. The final score is displayed at the end.

---

## How to Run
1. Make sure you have Python installed (version 3.x recommended).
2. Save the script as `true_or_false_quiz.py`.
3. Open your terminal or command prompt in the project directory.
4. Run the script:
   ```bash
   python true_or_false_quiz.py

---

## Example Output

---

## Technologies Used
- Python 3.x
- Custom Python classes for question and quiz logic
- Console/Terminal for user interaction
