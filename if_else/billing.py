customer_name = input("Enter the customer name: ")
membership = input("Enter yes / no: ").lower()
hours_used = int(input("Enter the hours: "))
time = input("Enter in day or night: ").lower()

if time == "day":
    if hours_used <=2:
        original_bill = hours_used * 100

    else:
        original_bill = (2*100) + ((hours_used -2) * 80)

elif time == "night":
    if hours_used <=2:
        original_bill = hours_used * 80

    else:
        original_bill = (2*100) + ((hours_used -2) * 60)

else :
    print("Invalid time")


discount = 0

if membership == "yes":
    if original_bill > 500:
        discount = original_bill * 0.20
    else:
        discount = original_bill * 0.10
elif membership == "no":
    discount = 0

else:
    print("Invalid membership status")
    exit()

