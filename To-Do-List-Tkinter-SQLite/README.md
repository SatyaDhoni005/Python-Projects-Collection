# Project - To-Do List Application

## Project Overview
The **To-Do List Application** is a Python-based GUI program that helps users manage their daily tasks efficiently.  
It allows adding, removing, and clearing tasks while storing them in a local SQLite database so that the tasks are retained even after closing the application.

This project uses **Tkinter** for the graphical interface and **SQLite** for persistent storage.

---

## Features
- **Add Tasks**: Quickly add new tasks with a simple text input.
- **Remove Tasks**: Delete a selected task from the list.
- **Delete All Tasks**: Clear all tasks in one click (with confirmation).
- **Persistent Storage**: Saves all tasks in a SQLite database.
- **User-Friendly GUI**: Simple, clean, and easy-to-use interface.
- **Exit Button**: Close the application with a single click.

---

## How It Works
1. On startup, the application loads all saved tasks from the SQLite database.
2. The user can:
   - Type a new task and click **Add** to save it.
   - Select an existing task and click **Remove** to delete it.
   - Click **Delete All** to clear all tasks (with confirmation).
3. Every change is reflected both in the GUI and the database instantly.
4. The user can exit the application using the **Exit / Close** button.

---

## How to Run
1. Make sure you have Python installed (version 3.x recommended).
2. Ensure the `listOfTasks.db` file is in the same directory as the script (or it will be created automatically).
3. Save the scripts:
   - `To_Do_List.py` (main application)
   - `db_explorer.py` (optional script to explore database content)
4. Open a terminal or command prompt in the project directory.
5. Run the application:
   ```bash
   python To_Do_List.py

---

## Example Output
<img width="1101" height="466" alt="Image" src="https://github.com/user-attachments/assets/b545818a-340c-4032-997f-3dfbac1f493f" />

---

## Technologies Used
- Python 3.x
- Tkinter → for the GUI interface
- SQLite3 → for persistent database storage
- messagebox module → for error and confirmation dialogs
- Listbox widget → to display the list of tasks
- OOP (Object-Oriented Programming) → to structure database and GUI code

---

## Database Details
- Database Name: listOfTasks.db
- Table Name: tasks
- Columns:
    - title (TEXT) → Task name
    - completed (INTEGER) → Completion status (0 = Not Completed)
