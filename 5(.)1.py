

count_positive = 0
count_negative = 0
total = 0
count = 0

while True:
    num = int(input("Enter an interger, the input ends if it is 0: "))
    if num == 0:
        break 

    if num > 0: 
       count_positive += 1
    elif num < 0:
        count_negative =+ 1

    total += num 
    count += 1

if count > 0:
        average = total / count
        print("The number of positive is: ", count_positive)
        print("The number of negative is:", count_negative)
        print("The total is", total)
        print("The avergage is", average)
else : 
        print("You didn't enter any number!!")
    
     

