# for i in range (1, 5):
#     j = 0
#     while j < i:
#         print(j, end = " ")
#         j += 1
#     print()

# i = 0 
# while i < 5:
#     for j in range (i, 1, -1):
#         print(j, end = " ")
#     print("***")
#     i += 1
# print()

# i = 5
# while i >= 1:
#     num = 1
#     for j in range(1, i + 1):
#         print(num, end ="xxx")
#         num *= 2
#     print()
#     i -= 1

# i = 1
# while i <= 5:
#     num = 1
#     for j in range (1, i + 1):
#         print(num, end = "G")
#         num += 2
#     print()

#     i += 1

# sum = 0 

# i =0.01
# for count in range(100):
#     sum += i
#     i = i + 0.01
# print("The sum is", sum)
# n1 = eval (input("Enter first integer: "))
# n2 = eval (input("Enter second integer: "))
# gcd = 1
# k = 2
# while k <= n1 and k <= n2:
#     if n1 % k == 0 and n2 % k == 0:
#         gcd = k 
#     k += 1

# print("The greatest common divisor for", n1, "and", n2, "is", gcd)

year = 0
tuition = 10000
while tuition < 20000: 
    year += 1
    tuition = tuition * 1.07
print("Tuition will be doubled in", year , "years")
print("Tuition will be $" + format(tuition, ".4f"), "in", year, "years")

# balance = 1000
# while True:
#     if balance < 9:
#         break
#     balance = balance - 9
# print ("Balance is", balance)

# for i in range(1, 4):
#     for j in range(1, 4):
#         if i * j > 2:
#             break
# print(i * j)
# print(i)
