# Write a Python program using nested for loops to generate an online shopping bill for multiple customers.

number_of_customer = int(input("Enter the number of customer: "))
highest_bill = 0
highest_customer = ''
total_sales = 0

for customer in range(1,number_of_customer+1):
    customer_name = input("Enter the customer name: ")

    total_bill = 0
    number_of_product = int(input("Enter the number_of_product: "))
    for product in range(1,number_of_product + 1):
        product_name = input("Enter the product name: ")
        quantity = int(input("Enter the quantity: "))
        price_per_item = int(input("Enter the price: "))


        product_total = quantity * price_per_item
       

        total_bill += product_total

    vat = total_bill * 0.13

    

    discount = 0

    if total_bill > 5000:
        discount_amt = total_bill * 0.10
        discount += discount_amt

    final_amount = total_bill + vat - discount

    total_sales += final_amount

    if final_amount > highest_bill:
        highest_bill = final_amount
        highest_customer = customer_name

    print("\n========== CUSTOMER BILL ==========")
    print("Customer Name :", customer_name)
    print("Total Bill    :", total_bill)
    print("VAT (13%)     :", vat)
    print("Discount      :", discount)
    print("Final Amount  :", final_amount)
    print("===================================")

        

average_sale = total_sales / number_of_customer

print("\n========== SALES REPORT ==========")
print("Total Customers      :", number_of_customer)
print("Highest Bill Customer:", highest_customer)
print("Highest Bill Amount  :", highest_bill)
print("Total Sales          :", total_sales)
print("Average Sale         :", average_sale)
        