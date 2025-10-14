
# 🧩 Personal Task Manager – Python Coursework

A four-stage **Software Development I (4COSC001W)** coursework project demonstrating fundamental programming concepts in Python, from simple list manipulation to GUI development with Tkinter.

---

## 📘 Overview

The **Personal Task Manager** is a functional application that allows users to:
* **Manage Tasks:** Add, view, update, and delete tasks (CRUD operations).
* **Handle Data:** Save and load tasks using both **plain text files** and the **JSON** format.
* **User Interface:** Provide a rich, interactive experience via a **Tkinter GUI** supporting viewing, searching, and sorting of tasks.

Each stage builds upon the last, progressively introducing essential topics like file handling, dictionaries, JSON, and Object-Oriented Programming (OOP).

---

## 🧱 Project Structure

```text
Personal-Task-Manager/
│
├── Stage_1_2_TaskManager.py  # Stage 1 & 2: Lists + Text File Handling
├── Stage_3_JSON_TaskManager.py # Stage 3: Dictionaries + JSON
├── Stage_4_GUI_TaskManager.py  # Stage 4: Tkinter GUI with OOP
│
├── mytasks.txt         # Text-based task storage for Stage 1–2
├── tasks.txt          # Text file storing data in JSON format for Stage 03
│
├──  Report.pdf        # Coursework documentation
│ 
└── LICENSE
````

-----

## 🧠 Stage Breakdown

### **Stage 1 & 2 – Lists & Text File Handling**

  * Implements the core **CRUD** (Create, Read, Update, Delete) operations.
  * Stores task data in memory using **Python lists**.
  * Persists data by saving and loading tasks from a plain **text file** (`mytasks.txt`).

### **Stage 3 – Dictionaries & JSON**

  * Refines the data structure by converting list-based storage into a **dictionary-based model**.
  * Implements robust data saving and loading using the **JSON** format (`tasks.txt`).
  * Enhances data integrity and error handling.

### **Stage 4 – Tkinter GUI (Classes & Objects)**

  * Develops a full-featured graphical user interface using **Tkinter**.
  * Displays tasks in a tabular format using the **Treeview** widget.
  * Integrates advanced features: **filtering**, **searching**, and **sorting** by task name, priority, and due date.
  * Uses **Object-Oriented Programming** principles with `Task`, `TaskManager`, and `TaskManagerGUI` classes.

-----

## 💻 How to Run

Ensure you have **Python 3.x** installed on your system.

## 🪄 Option 1 – Run from Terminal


### Run the console-based version
```bash
python Stage_1_2_TaskManager.py
```

### Run the GUI version (Stage 4)
```bash
python Stage_4_GUI_TaskManager.py
```

## 🧰 Option 2 – Run from VS Code or IDE

1.  Open the desired `.py` file (e.g., `Stage_4_GUI_TaskManager.py`).
2.  Click the **Run** button (▶️) or use the run command specific to your IDE (e.g., `F5`).
3.  Interact with the program via terminal prompts or the graphical user interface.

### ⚙️ Requirements

The project relies on standard Python libraries. **Tkinter** is typically included with a standard Python installation. If required, you can ensure it's installed:

```bash
pip install tk
```

-----

## 🧪 Testing and Validation

  * **CRUD Operations:** Tested for both valid and invalid input scenarios.
  * **File Handling:** Verified the integrity of file save/load functionality using multiple task entries for both text and JSON formats.
  * **GUI Functionality:** Thoroughly tested filtering, searching, and sorting capabilities across key fields (task name, priority, due date).



-----

## 📑 Coursework Info

| Detail | Value |
| :--- | :--- |
| **Module** | 4COSC001W – Software Development I |
| **Instructor** | Mr. P. Guganathan |
| **Student** | Zubair Murshid |
| **Academic Year** | 2024/25 |

-----

## 🧾 License and Author

This project is released under the **MIT License** (see `LICENSE` file for details). You are welcome to use or reference this work for educational and personal learning purposes.

**Author:** Zubair Murshid  
**Email:** zubairmurshid69@gmail.com  
**GitHub:** https://github.com/ZubairMurshid

```

```
