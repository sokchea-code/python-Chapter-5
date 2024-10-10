import random 
import time

correct_Count = 0
count = 0
total_question = 10

startTime = time.time()
while count < total_question:
    num1= random.randint(1, 15)
    num2= random.randint(1, 15)
    if num1>num2:
        num1, num2 = num2, num1
    answer = eval(input(f"What is {num1} + {num2} ? "))
    if num1 + num2 == answer:
        print("Correct!")
        correct_Count += 1
    else:
        print("Inccorect!")
    count += 1

endTime = time.time()
testTime= int(endTime - startTime)
print("Correct count is:", correct_Count)
print("Test time is:", testTime, "Second")




