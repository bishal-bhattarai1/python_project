# Restaurant Management & Billing System

number_of_tables = int(input("Enter the number of tables: "))

highest_bill = 0
highest_table = 0
total_restaurant_sales = 0
total_customers = 0

for tables in range(1,number_of_tables+1):
    table_number = int(input("Enter the table_number: "))
    number_of_customer = int(input("Enter the number of customer: "))
    total_customers += number_of_customer
    table_bill = 0

    for customer in range(1,number_of_customer+1):
            customer_name = input("Enter the customer name: ")
            number_of_food_items = int(input("Enter the number of food items: "))

            customer_bill = 0

            for food_items in range(number_of_food_items):
                  food_name = input("Enter the food name: ")
                  quantity = int(input("Enter the quantity: "))
                  price_per_item = int(input("Enter the price per item: "))

                  item_total = quantity * price_per_item

                  customer_bill += item_total

            table_bill+= customer_bill

    vat = table_bill * 0.13

    service_charge = table_bill * 0.05

    discount = 0
    if table_bill > 20000:
        discount = table_bill * 0.10


    final_bill = table_bill + vat + service_charge - discount
    total_restaurant_sales += final_bill

    if final_bill > highest_bill:
            highest_bill = final_bill
            highest_table = table_number

    print("\n========== TABLE BILL ==========")
    print("Table Number:", table_number)
    print("Total Customers:", number_of_customer)
    print("Table Bill:", table_bill)
    print("VAT:", vat)
    print("Service Charge:", service_charge)
    print("Discount:", discount)
    print("Final Bill:", final_bill)
    print("================================")

average_bill = total_restaurant_sales / number_of_tables

print("\n========== RESTAURANT REPORT ==========")
print("Total Tables:", number_of_tables)
print("Total Customers:", total_customers)
print("Highest Billing Table:", highest_table)
print("Highest Bill Amount:", highest_bill)
print("Total Restaurant Sales:", total_restaurant_sales)
print("Average Table Bill:", average_bill)



                