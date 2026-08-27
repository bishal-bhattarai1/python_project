students = []

# Function to add new student
def add_student():
    student = {}
    student['id'] = input("Enter student ID: ")
    student['name'] = input("Enter student name: ")
    student['age'] = input("Enter student age: ")
    student['grade'] = input("Enter student grade: ")
    students.append(student)
    print(student)
    print("✅ Student added successfully!\n")


# view students

def view_students():
    if not students:
        print("No Student Found.")
        return  # tala ko code lai chalna diday naa 
    for student in students:
        print(f"ID: {student["id"]}, name: {student["name"]}, age: {student["age"]}, grade: {student["grade"]}")

# view_students()


# Serach Student 
def search_student():
    query = input("Enter id or name for search: ")
    found = False
    for student in students:
        if query == student["id"] or query.lower() == student["name"].lower():
            print(f"Student Found: ID: {student["id"]}, name: {student["name"]}, age: {student["age"]}, grade: {student["grade"]}")
            found = True

    if not found:
        print("Student not Found. \n")
        




#update 
# query -> student["id"]
def update_student():
    query = input("Enter the id for search : ")
    for student in students:
        if student["id"] == query:
            student["name"] = input("Enter the student name: ")
            student["age"] = input("Enter the student age: ")
            student["grade"] = input("Enter the student grade: ")
            print("Student Update.")
            return
    print("Student not found.")


# delete
def delete_student():
    query = input("Enter the id to delete: ")
    for student in students:
        if student["id"] == query:
            students.remove(student)
            print("Student Deleted Sucessfully")
            return
    print("Student not found.")


#to find total number fo students
def total_students():
    print(f"Total number of students is",len(students))


# main menu

def main_menu():
    while True:
        print("\n==========Student Mangement System ==========")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Total Students")
        print("7. Exit")
        print("======================================\n")
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif total_students():
            total_students()
        elif choice == "7":
            print("Existing Program. Good Bye!!")
            break
        else:
            print("Invalid Choice. Try again")

main_menu()