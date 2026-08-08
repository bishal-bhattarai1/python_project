# Employee Performance & Bonus System

number_of_employee = int(input("Enter the number of employee: "))


highest_salary = 0
highest_employee = ""

total_salary = 0
excellent_employee = 0
no_bonus_employee = 0

basic_salary = 30000

for employee in range(1,number_of_employee+1):
    employee_name = input("Enter the employee name: ")
    employee_id = input("Enter the employee id: ")
    number_of_project_completed = int(input("Enter the number of project completed: "))
    peformance_score = int(input("Enter the score from 0 - 100: "))
    years_of_experience = int(input("Enter the years of experience: "))

    if peformance_score > 90:
        performance_status = "Excellent"
        excellent_employee += 1

    elif peformance_score > 75:
        performance_status = "Very Good"
        excellent_employee += 1

    elif performance_status > 60:
        performance_status = "Good"
        excellent_employee +=1

    elif performance_status > 40:
        performance_status = "Average"
        excellent_employee +=1 

    else:
        performance_status = "Poor"
        excellent_employee += 1

    bonus_amt = 0
    
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
