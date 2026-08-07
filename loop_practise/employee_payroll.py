# Employee Payroll Management System

number_of_employee = int(input("Enter the number of employee: "))
total_employee  = number_of_employee
highest_salary = 0
highest_name = ''
total_salary = 0

for employee in range(1,number_of_employee+1):
    employee_name = input("Enter the employee name: ")
    employee_id = input("Enter the employee id: ")
    days_of_worked = int(input("Enter the day worked: "))

    gross_salary = 0
    for working_day in range(1,days_of_worked+1):
        hours_worked = int(input("Enter the hours worked: "))
        hourly_rate = int(input("Enter the hourly rate: "))

        daily_salary = hours_worked * hourly_rate

        gross_salary += daily_salary

    tax = 0
    if gross_salary > 30000:
        tax = gross_salary * 0.10

    else:
        tax = gross_salary * 0.05

    bonus = 0
    if gross_salary > 40000:
        bonus = 2000

    net_salary = gross_salary - tax + bonus

    if net_salary > highest_salary:
        highest_salary = net_salary
        highest_name = employee_name

    total_salary += net_salary
        


    print("\n========== Employee Payroll ==========")
    print("Employee Name :", employee_name)
    print("Employee ID   :", employee_id)
    print("Gross Salary  :", gross_salary)
    print("Tax           :", tax)
    print("Bonus         :", bonus)
    print("Net Salary    :", net_salary)
    print("======================================")

average_net_salary = total_salary / number_of_employee

print("\n========== Payroll Report ==========")
print("Total Employee     :", total_employee)
print("Highest Salary     :", highest_name)
print("Highest Net Salary :", highest_salary)
print("Total Payroll      :", total_salary)
print("Average Salary     :", average_net_salary)

