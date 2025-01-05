#ﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩProblem2Mainﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ♡ﮩ٨ـﮩﮩ٨ـ
# problem 2 is to to develop code for processing data for a group of
# students in a University class.

#I Decided to organise the problem into tasks for clarity and ease of debugging.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Imports~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import matplotlib.pyplot as plt  # Matplotlib for plotting
import numpy as np  # NumPy for numerical calculations
import csv
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Task 1: Define the Student class with basic attributes
# Define a class to represent each student with their basic information and grades.
class Student:
    # Initialize a student object with ID, name, address, and placeholders for grades.
    def __init__(self, student_id, name, address):
        self.student_id = student_id  # Unique identifier for a student.
        self.name = name  # Student's full name.
        self.address = address  # Student's home address.
        self.programming_grade = None  # Placeholder for programming grade, to be filled later.
        self.digital_grade = None  # Placeholder for digital skills grade, to be filled later.

    # This method returns a formatted string representation of a student's information.
    def __str__(self):
        return (f"Student ID: {self.student_id}\n"
                f"Name: {self.name}\n"
                f"Address: {self.address}\n"
                f"Programming Grade: {self.programming_grade}\n"
                f"Digital Grade: {self.digital_grade}")

    # Method to assign grades to a student. It takes programming and digital grades as arguments.
    def add_grades(self, programming_grade, digital_grade):
        self.programming_grade = programming_grade  # Assign the programming grade.
        self.digital_grade = digital_grade  # Assign the digital grade.

    # Calculate and return the average of the available grades.
    def get_average_grade(self):
        grades = [g for g in [self.programming_grade, self.digital_grade] if g is not None]  # Filter out 'None' values.
        return sum(grades) / len(grades) if grades else 0  # Return the average if there are grades, otherwise return 0.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Task 2: Function to read student data from a text file and create Student objects
# Function to load student data from a text file and create Student objects for each entry.
def read_student_data(file_path):
    students = {}  # Create an empty dictionary to hold student data.
    with open(file_path, 'r') as file:  # Open the file for reading.
        for line in file:  # Iterate over each line in the file.
            parts = line.strip().split()  # Split the line into parts.
            student_id = parts[0]  # The first part is the student ID.
            name = ' '.join(parts[1:-2])  # Join the middle parts as the name.
            address = ' '.join(parts[-2:])  # The last two parts form the address.
            students[student_id] = Student(student_id, name, address)  # Create a Student object and add it to the dictionary.
    return students  # Return the dictionary of students.

def read_programming_grades(students, file_path):
    with open(file_path, 'r') as file:  # Open the file for reading.
        for line in file:  # Iterate over each line in the file.
            student_id, grade = line.strip().split()  # Split the line into student ID and grade.
            if student_id in students:  # Check if the student ID is in the dictionary.
                students[student_id].programming_grade = int(grade)  # Update the programming grade for the student.

# Similar to the above function, but for reading digital grades.
def read_digital_grades(students, file_path):
    with open(file_path, 'r') as file:  # Open the file for reading.
        for line in file:  # Iterate over each line.
            student_id, grade = line.strip().split()  # Split the line into student ID and grade.
            if student_id in students:  # Check if the student ID exists in the dictionary.
                students[student_id].digital_grade = int(grade)  # Update the digital grade for the student.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Task 3: Functions to read grades from files and update Student objects

# Function to load student data from a text file and create Student objects for each entry.
def read_student_data(file_path):
    students = {}  # Create an empty dictionary to hold student data.
    with open(file_path, 'r') as file:  # Open the file for reading.
        for line in file:  # Iterate over each line in the file.
            parts = line.strip().split()  # Split the line into parts.
            student_id = parts[0]  # The first part is the student ID.
            name = ' '.join(parts[1:-2])  # Join the middle parts as the name.
            address = ' '.join(parts[-2:])  # The last two parts form the address.
            students[student_id] = Student(student_id, name, address)  # Create a Student object and add it to the dictionary.
    return students  # Return the dictionary of students.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 4~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Task 4: Managing student data

# Add a new student record to the dictionary. If the student already exists, notify the user.
def add_student(students, student_id, name, address):
    if student_id not in students:  # Check if the student ID does not exist in the dictionary.
        students[student_id] = Student(student_id, name, address)  # Add the new student.
        return f"Student {student_id} added successfully."
    else:
        return f"Student {student_id} already exists."  # Notify that the student already exists.

# Remove a student record from the dictionary. If the student does not exist, notify the user.
def remove_student(students, student_id):
    if student_id in students:  # Check if the student ID exists in the dictionary.
        del students[student_id]  # Delete the student.
        return f"Student {student_id} removed successfully."
    else:
        return f"Student {student_id} not found."  # Notify that the student was not found.

# Modify an existing student's data. This allows changing the name and/or address.
def modify_student(students, student_id, name=None, address=None):
    if student_id in students:  # Check if the student ID exists.
        if name:
            students[student_id].name = name  # Update the name if provided.
        if address:
            students[student_id].address = address  # Update the address if provided.
        return f"Student {student_id} modified successfully."
    else:
        return f"Student {student_id} not found."  # Notify that the student was not found.


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 5~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Task 5: Plot Grade Distributions
# Function to plot the grade distributions as CDF and PDF.
def plot_grade_distributions(students):
    # Extract programming and digital grades from the students dictionary.
    programming_grades = [s.programming_grade for s in students.values() if s.programming_grade is not None]
    digital_grades = [s.digital_grade for s in students.values() if s.digital_grade is not None]

    # Nested function to plot CDF and PDF for a set of grades.
    def plot_distribution(grades, module_name):
        grades = np.array(grades)  # Convert grades list to a NumPy array for processing.
        sorted_grades = np.sort(grades)  # Sort the grades in ascending order.

        # Plot CDF
        plt.figure(figsize=(10, 4))  # Set figure size.
        plt.subplot(1, 2, 1)  # Position the first subplot.
        plt.plot(sorted_grades, np.arange(1, len(sorted_grades) + 1) / len(sorted_grades))  # Plot the CDF.
        plt.title(f'{module_name} Grades CDF')  # Title for the CDF plot.
        plt.xlabel('Grade')  # X-axis label.
        plt.ylabel('CDF')  # Y-axis label.

        # Plot PDF
        plt.subplot(1, 2, 2)  # Position the second subplot.
        plt.hist(grades, bins=10, density=True, alpha=0.6, color='pink')  # Plot the PDF.
        plt.title(f'{module_name} Grades PDF')  # Title for the PDF plot.
        plt.xlabel('Grade')  # X-axis label.
        plt.ylabel('Density')  # Y-axis label.

        plt.suptitle(f'{module_name} Grades Distribution')  # Main title for both plots.
        plt.tight_layout()  # Adjust layout to prevent overlap.
        plt.show()  # Display the plots.

    # Call the plot_distribution function for both sets of grades.
    plot_distribution(programming_grades, 'Programming')
    plot_distribution(digital_grades, 'Digital')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 6~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Task 6: Export Data to a CSV File
# Function to export the student data, including grades, to a CSV file.
def export_students_to_csv(students, filename='student_data_with_grades.csv'):
    with open(filename, mode='w', newline='') as file:  # Open or create the file for writing.
        writer = csv.writer(file)  # Create a CSV writer object.
        writer.writerow(['Student ID', 'Name', 'Address', 'Programming Grade', 'Digital Grade', 'Average Grade'])  # Write the header row.

        for student_id, student in students.items():  # Iterate over each student in the dictionary.
            writer.writerow([  # Write a row for each student.
                student.student_id,
                student.name,
                student.address,
                student.programming_grade,
                student.digital_grade,
                student.get_average_grade()  # Calculate and include the average grade.
            ])

    print(f'Data successfully exported to {filename}')  # Notify the user of successful export.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Task 7~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Task 7: Menu system for interacting with the student database
def menu():
    students = read_student_data('student_data.txt')
    read_programming_grades(students, 'gradesprogramming.txt')
    read_digital_grades(students, 'gradesdigital.txt')

    while True:
        print("\n--- ˗ˋˏ ♡ ˎˊ˗ Student Database Menu ˗ˋˏ ♡ ˎˊ˗ ---")
        print("1: Print all students")
        print("2: Add a New Student")
        print("3: Remove a Student")
        print("4: Modify Student Details")
        print("5: Print a Single Student's Details")
        print("6: Plot Graphs")
        print("7: Save Data to File")
        print("0: Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            for student_id, student in students.items():
                print(student)  # Print details of each student.
        elif choice == '2':
            student_id = input("Enter student ID: ")
            name = input("Enter student's full name: ")
            address = input("Enter student's address: ")
            print(add_student(students, student_id, name, address))
        elif choice == '3':
            student_id = input("Enter student ID to remove: ")
            print(remove_student(students, student_id))
        elif choice == '4':
            student_id = input("Enter student ID to modify: ")
            name = input("Enter student's new full name (or leave blank): ")
            address = input("Enter student's new address (or leave blank): ")
            print(modify_student(students, student_id, name, address))
        elif choice == '5':
            student_id = input("Enter student ID to print details: ")
            if student_id in students:
                print(students[student_id])  # Print details for the specified student.
            else:
                print("Student not found.")
        elif choice == '6':
            plot_grade_distributions(students)  # Call the plotting function.
        elif choice == '7':
            export_students_to_csv(students, 'student_data_with_grades.csv')  # Export data to CSV.
            print("Data saved successfully.")
        elif choice == '0':
            print("Exiting the program.")
            break  # Correctly placed break statement to exit the while loop.
        else:
            print("Invalid choice. Please try again.")

menu()