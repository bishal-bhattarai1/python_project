# Library Management System

number_of_members = int(input("Enter the number of member: "))

total_member = number_of_members
highest_fine = 0
highest_fine_member = ""

for member in range(number_of_members):
    member_name = input("Enter the member name: ")

    number_of_books_borrowed = int(input("Enter the number of books borrowed: "))

    total_book_borrowed += number_of_books_borrowed
    total_fine = 0

    for books in range(number_of_books_borrowed):
        book_name = input("Enter the book name: ")

        number_of_days_borrowed = int(input("Enter the number of days boks borrowed: "))

        fine = 0
      

        if  number_of_days_borrowed <= 7:
            fine = 0

        elif number_of_books_borrowed <=14:
            fine = (number_of_days_borrowed - 7)*20
        else:
            fine = (7 * 20) +  ((number_of_days_borrowed - 14)*50)

        
        total_fine += fine
        
    total_fine_collected += total_fine

    if total_fine > highest_fine:
            highest_fine = total_fine
            highest_fine_member = member_name

    print("\n========== Member Display ==========")
    print("Member Name: ", member_name)
    print("Book Borrowed: ", number_of_books_borrowed)
    print("Total Fine: ", total_fine)
    print("----------------------------------------")

average_fine = total_fine_collected/number_of_members





print("\n========== Library Report ==========")
print("Total Members:", total_member)
print("Total Books Borrowed:", total_book_borrowed)
print("Highest Fine Member:", highest_fine_member)
print("Highest Fine Amount:", highest_fine)
print("Total Fine Collected:", total_fine_collected)
print("Average Fine:", average_fine)