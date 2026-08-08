# Student Result System

subject = ["Math","Science","English","Social","Computer"]
student_name = input("Enter the Student Name: ")
total_marks = 0
for i in subject:
    marks_number = int(input(f"Enter the {i} marks: "))
    total_marks += marks_number


if marks_number > 40:
    marks_staus = "Passed"
else:
    marks_staus = "Failed"


percentage = (total_marks /500) * 100

print("\n ========== Result =========")
print("Student Name: ",student_name)
print("Total Marks: ",total_marks)
print("Percentage: ",percentage)
print("Marks Status: ",marks_staus)
print("================================")


