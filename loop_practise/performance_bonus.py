# Employee Performance & Bonus System

number_of_employee = int(input("Enter the number of employee: "))


highest_salary = 0
highest_employee = ""

total_salary = 0

for employee in range(1,number_of_employee+1):
    employee_name = input("Enter the employee name: ")
    employee_id = input("Enter the employee id: ")
    number_of_project_completed = int(input("Enter the number of project completed: "))
    peformance_score = int(input("Enter the score from 0 - 100: "))
    years_of_experience = int(input("Enter the years of experience: "))

    if peformance_score > 90:
        performance_status = "Excellent"
    elif peformance_score > 75:
        performance_status = "Very Good"
    elif performance_status > 60:
        performance_status = "Good"
    elif performance_status > 40:
        performance_status = "Average"
    else:
        performance_status = "Poor"

    bonus_amt = 0
    basic_salary = 30000
    if peformance_score >=75:
        if years_of_experience >= 5:
            bonus_amt = basic_salary * 0.20
        else:
            bonus_amt = basic_salary * 0.10
    else:
        if peformance_score < 75:
            if number_of_project_completed >=5:
                bonus_amt = basic_salary * 0.05
            else:
                bonus_amt = bonus_amt
    
    final_salary = basic_salary + bonus_amt


print("\n===========Bonus System ==========")
print("Total Employee",number_of_employee)
print("Highest Performing Employee",)    
