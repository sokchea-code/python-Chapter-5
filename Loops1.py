# import math 
# rarius = int (input())
# while radius < 10:
#     area = radius **2 * math.pi
#     print(f"(Circle area when {radius} is {area:.2f})")

# i = 0 
# while 1 < 10 :
#     print(i) 
    
# for i in range(1,10): 
#     #print(i, "|", end = '')
#     print()
#     for j in range(1,10):
#         print(format( i * j, "4d"), end = "")

sum = 0 
number = 0 

while number < 20:
    number += 1
    if number == 10: #or number == 11:
       break
    sum += number 
  
print("The number is", number )
print("The sum is", sum)
    