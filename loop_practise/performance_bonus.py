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
    performance_score = int(input("Enter the score from 0 - 100: "))
    years_of_experience = int(input("Enter the years of experience: "))

    if performance_score > 90:
        performance_status = "Excellent"
        excellent_employee += 1

    elif performance_score > 75:
        performance_status = "Very Good"
        excellent_employee += 1

    elif performance_score > 60:
        performance_status = "Good"
        excellent_employee +=1

    elif performance_score > 40:
        performance_status = "Average"
        excellent_employee +=1 

    else:
        performance_score = "Poor"
        excellent_employee += 1

    bonus_amt = 0
    
    if performance_score >=75:
        if years_of_experience >= 5:
            bonus_amt = basic_salary * 0.20
        else:
            bonus_amt = basic_salary * 0.10
    else:
        if performance_score < 75:
            if number_of_project_completed >=5:
                bonus_amt = basic_salary * 0.05
            else:
                bonus_amt = bonus_amt
    
    final_salary = basic_salary + bonus_amt

    if final_salary > highest_salary:
        highest_salary = final_salary
        highest_employee = employee_name

    total_salary += final_salary

    # Employee Report
    print("\n=========== Employee Report ===========")
    print("Employee Name:", employee_name)
    print("Employee ID:", employee_id)
    print("Projects Completed:", number_of_project_completed)
    print("Performance Score:", performance_score)
    print("Performance Status:", performance_status)
    print("Years of Experience:", years_of_experience)
    print("Basic Salary:", basic_salary)
    print("Bonus Amount:", bonus_amt)
    print("Final Salary:", final_salary)
    print("========================================")


# Final Report
average_salary = total_salary / number_of_employee

print("\n=========== Final Report ===========")
print("Total Employees:", number_of_employee)
print("Highest Performing Employee:", highest_employee)
print("Highest Final Salary:", highest_salary)
print("Total Salary Paid:", total_salary)
print("Average Final Salary:", average_salary)
print("Excellent Employees:", excellent_employee)
print("Employees With No Bonus:", no_bonus_employee)
print("====================================")
