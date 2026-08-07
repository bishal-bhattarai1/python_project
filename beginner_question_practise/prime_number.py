#prime_number

number = int(input("Enter the number: "))

print ("\n ------ Number ---------- ")
if number <= 1:
    print(f"Give number:- {number} is not prime number.")
else:
    for i in range(2,number):
        if number%i == 0:
            print(f"Given number:- {number} is not prime number")
            break
    else:
        print(f"Given number:- {number} is prime number.")


print ("------------------------ ")
