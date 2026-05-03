# List to store all student records
students = []

# ---- FUNCTION 1: Display Menu ----
def displayMenu():
    print("\n----- Student Record Manager -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student by ID")
    print("4. Show Statistics")
    print("5. Save to File")
    print("6. Load from File")
    print("7. Exit")

# ---- FUNCTION 2: Add Student ----
def addStudent():
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")

    while True:
        age = input("Enter Age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Invalid age! Please enter a number.")

    while True:
        marks = input("Enter Marks: ")
        if marks.isdigit() and 0 <= int(marks) <= 100:
            marks = int(marks)
            break
        else:
            print("Invalid marks! Please enter a number between 0 and 100.")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "marks": marks
    }
    students.append(student)
    print("Student added successfully!")

# ---- FUNCTION 3: Display All Students ----
def displayStudents():
    print("\n--- All Student Records ---")
    if len(students) == 0:
        print("No students found!")
        return
    print("-" * 45)
    print(f"{'ID':<10} {'Name':<15} {'Age':<6} {'Marks':<6}")
    print("-" * 45)
    for student in students:
        print(f"{student['id']:<10} {student['name']:<15} {student['age']:<6} {student['marks']:<6}")
    print("-" * 45)

# ---- FUNCTION 4: Search Student ----
def searchStudent():
    print("\n--- Search Student ---")
    search_id = input("Enter Student ID to search: ")
    
    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found!")
            print("-" * 45)
            print(f"{'ID':<10} {'Name':<15} {'Age':<6} {'Marks':<6}")
            print("-" * 45)
            print(f"{student['id']:<10} {student['name']:<15} {student['age']:<6} {student['marks']:<6}")
            print("-" * 45)
            return
    
    print(f"No student found with ID: {search_id}")

# ---- FUNCTION 5: Calculate Statistics ----
def calculateStatistics():
    print("\n--- Student Statistics ---")
    
    if len(students) == 0:
        print("No students found!")
        return
    
    marks_list = [student["marks"] for student in students]
    
    highest = max(marks_list)
    lowest = min(marks_list)
    average = sum(marks_list) / len(marks_list)
    
    print(f"Highest Marks : {highest}")
    print(f"Lowest Marks  : {lowest}")
    print(f"Average Marks : {average:.2f}")

# ---- FUNCTION 6: Save to File ----
def saveToFile():
    print("\n--- Save to File ---")
    
    if len(students) == 0:
        print("No students to save!")
        return
    
    file = open("students.txt", "w")
    
    for student in students:
        line = f"{student['id']},{student['name']},{student['age']},{student['marks']}\n"
        file.write(line)
    
    file.close()
    print("Records saved to students.txt successfully!")

# ---- FUNCTION 7: Load from File ----
def loadFromFile():
    print("\n--- Load from File ---")
    
    try:
        file = open("students.txt", "r")
        students.clear()
        
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                student = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": int(parts[2]),
                    "marks": int(parts[3])
                }
                students.append(student)
        
        file.close()
        print(f"Records loaded successfully! {len(students)} student(s) found.")
    
    except FileNotFoundError:
        print("No saved file found! Please save records first.")

# ---- MAIN PROGRAM ----
def main():
    while True:
        displayMenu()
        choice = input("\nEnter your choice: ")

        if choice == "1" :
            addStudent()
        elif choice == "2":
            displayStudents()
        elif choice == "3":
            searchStudent()
        elif choice =="4":
            calculateStatistics()
        elif choice == "5":
            saveToFile()
        elif choice == "6":
            loadFromFile()
        elif choice == "7":
            print("Bye Bye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

            

