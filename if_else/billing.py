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

bill_after_discount = original_bill - discount

vat = 0
if bill_after_discount > 700:
    vat = bill_after_discount * 0.13

final_bill = bill_after_discount + vat



print(f"Customer Name : {customer_name}")
print(f"Membership : {membership.capitalize()}")
print(f"Hours Used : {hours_used}")
print(f"Time : {time.capitalize()}")
print(f"Original Bill : Rs. {original_bill:.2f}") 
print(f"Discount : Rs. {discount:.2f}")
print(f"Bill After Discount: Rs. {bill_after_discount:.2f}") 
print(f"VAT (13%) : Rs. {vat:.2f}")
print(f"Final Bill : Rs. {final_bill:.2f}")