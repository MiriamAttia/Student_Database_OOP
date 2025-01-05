# Problem 2: Development of a Student Database Using Object-Oriented Programming

## Project Overview
This project is part of the EE2702 Computer Science and Programming coursework at City University of London. It involves creating a student database management system using Object-Oriented Programming (OOP). The program processes student data, integrates grades from different modules, calculates average grades, visualizes grade distributions, and provides an interactive menu-driven interface for managing student records.

---

## Features

1. **Data Parsing**:
   - Reads student data from `student_data.txt` and loads it into `Student` objects.
   - Reads and integrates grades from `gradesprogramming.txt` and `gradesdigital.txt`.

2. **Menu-Driven User Interface**:
   - View all students.
   - Add new student records.
   - Remove existing students.
   - Modify student details.
   - View details of an individual student.

3. **Grade Management**:
   - Calculates the average grade for each student.
   - Visualizes grade distributions using:
     - Cumulative Distribution Function (CDF).
     - Probability Density Function (PDF).

4. **Data Export**:
   - Saves the consolidated student database, including grades, into an external file (`student_data_with_grades.csv`).

---

## How to Run

### Prerequisites
- Python 3.x installed.
- Required libraries: `matplotlib`, `numpy`.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/MiriamAttia/Student_Database_OOP.git
