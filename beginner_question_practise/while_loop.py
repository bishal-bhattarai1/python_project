# 3 step, initial value, condition, update/change
# 1 to 10

i = 1  #initial value

while i <= 10:  #condition
    print(i)

    i += 1 # update/change

#######################################################################



#Even and ODD Number
num = 1

even_number = []
odd_number = []

while num <= 20:
    if num%2 == 0:
        even_number.append(num)
    else:
        odd_number.append(num)
    num += 1

print("Even Number",even_number)
print("Odd Number",odd_number)