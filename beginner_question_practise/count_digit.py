number =  int(input("Enter the number: "))  
count = 0

num  = number   

while num > 0:
    num = num // 10
    count += 1

print("Number of Digit Count is", count)