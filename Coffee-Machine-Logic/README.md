# Project - Coffee Machine Logic

## Project Overview
The **Coffee Machine Logic** project is a Python console-based simulation of a coffee vending machine.  
It allows users to choose from three coffee types — Espresso, Latte, and Cappuccino — pay using coins, and receive the coffee if resources and payment are sufficient. The program also manages stock levels and keeps track of earnings.

---

## Features
- Menu with three coffee options:
  - Espresso – ₹50
  - Latte – ₹80
  - Cappuccino – ₹100
- Ability to view the current stock of ingredients and money (`report` command).
- Checks ingredient availability before preparing coffee.
- Accepts coins in ₹10, ₹5, ₹2, and ₹1 denominations.
- Calculates and returns change if the user pays more than the cost.
- Updates resources after each purchase.
- Allows exiting the program anytime.

---

## How It Works
1. The menu is displayed to the user.
2. The user selects a coffee type or chooses `report` to view current stock, or `no` to exit.
3. The program checks if enough ingredients are available for the selected coffee.
4. The user is prompted to insert coins.
5. If the payment is:
   - **Less than cost** → Transaction is cancelled, and the amount is refunded.
   - **Equal to or more than cost** → Coffee is prepared, change is returned if applicable, and resources are updated.
6. The loop continues until the user chooses to exit.

---

## How to Run
1. Make sure Python is installed (version 3.x recommended).
2. Save the script as `coffee_machine.py`.
3. Open a terminal or command prompt in the project directory.
4. Run the script:
   ```bash
   python coffee_machine.py

---

## Example Output
<img width="1296" height="860" alt="Image" src="https://github.com/user-attachments/assets/77298757-d22b-46d8-848e-454d74182d90" />

---

## Technologies Used
- Python 3.x
- Dictionaries for menu and resources management
- Loops and conditionals for game logic
- Console/Terminal for user interaction
