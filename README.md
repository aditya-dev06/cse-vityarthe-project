# cse-vityarthe-project

# 🏥 Hospital Management System (CLI)

## 📌 Overview
This is a lightweight, command-line based **Hospital Management System** built using Python. It is designed to demonstrate the fundamentals of **Object-Oriented Programming (OOP)** and data management using Python's built-in data structures (Dictionaries).

The system allows hospital staff to admit patients, view current records, search for specific individuals, and discharge patients when they recover.

## 🚀 Features
The program covers the essential **CRUD** (Create, Read, Delete) operations:
* **Admit Patient (Create):** Register a new patient with a unique ID, name, age, and disease description. The system automatically records the admission date.
* **View All Patients (Read):** Display a formatted table of all patients currently admitted to the hospital.
* **Search Patient (Read):** innovative lookup feature to find patient details using their unique ID.
* **Discharge Patient (Delete):** Remove a patient's record from the active system upon discharge.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Data Storage:** In-Memory Python Dictionary (`dict`)
* **Interface:** Command Line Interface (CLI)
* **Modules Used:** `time` (for auto-generating dates)

## ⚙️ Setup & Execution
1.  **Prerequisites:** Ensure you have Python installed on your machine.
    * Check by running: `python --version`
2.  **Installation:** No external libraries are required. Just download the script.
3.  **Running the Code:**
    Open your terminal or command prompt, navigate to the folder containing the file, and run:
    ```bash
    python hospital_system.py
    ```

## 📖 Usage Guide
1.  **Start the Program:** You will see the main menu with 5 options.
2.  **Admit a Patient:** Select Option `1`. You must provide a **Unique ID** (e.g., `P101`). If you try to use an existing ID, the system will alert you to prevent duplicates.
3.  **View List:** Select Option `2` to see who is currently in the hospital.
4.  **Discharge:** Select Option `4` when a patient is ready to leave. Enter their ID, and their data will be removed from the active memory.
5.  **Exit:** Select Option `5` to close the application.
    * *Note: Since this uses RAM for storage, all data is reset when the program closes.*

## 🔮 Future Improvements
* [ ] Add file handling (CSV/JSON) to save patient data permanently.
* [ ] Add a "Doctor Allocation" feature to assign doctors to patients.
* [ ] Add input validation to ensure Age is a number.

---
*Created by [Your Name/ID]*
