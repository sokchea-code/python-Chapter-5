
# import random 
# import time 
# correctCount = 0 
# count = 0 
# Number_of_Questions = 5

# startTime = time.time()
# while count < Number_of_Questions: 
#     number1 = random.randint(0, 9)
#     number2 = random.randint(0, 9) 

#     if number1 < number2: 
#         number1 , number2 = number2 , number1 
    
#     answer = eval(input("What is " + str(number1) + "-" + str(number2) + " ? "))

#     if number1 - number2 == answer: 
#         print("You are correct!")
#         correctCount += 1
#     else: 
#         print("Your number is wrong. \n", number1, "-", 
#               number2, "is", number1 - number2)
# endTime = time.time()
# testTime= int(endTime - startTime)
# print("Correst count is", correctCount, "out of", Number_of_Questions, "\nTest time is", testTime, "seconds")



# continueLoop = 'Y'
# while continueLoop == 'Y':
#     continueLoop= input("Enter Y to continue and N to quit: ")
   
# data = eval(input("Enter an integer (the input ends "+" if it is 0): "))

# sum = 0 
# while data != 0 :
#     sum += data 
#     data = eval(input ("Enter an integer (the input ends "+" if it is 0):"))
# print("The sum is", sum)


# for j in range (1,2): 
#     j = 0
# while j < 3: 
#     print(j, end= "")
#     j += 1



# number = eval(input("Enter an integer: "))
# max = number 

# while number != 0: 
#     number = eval (input("Enter an integer: "))
#     if number > max:
#         max = number 
# print ("max is", max)
# print ("number is", number )

# number = 0
# sum = 0 
# for count in range(5):
#     number = eval (input("Enter an integer: "))
#     sum += number 
# print("sum is", sum )
# print("Count is", count)

# #For loops
# sum = 0
# for i in range (1001):
#     sum = sum + i
# #Conver to while loops
# sum = 0
# i = 0 

# while i < 1001:
#     sum += i
#     i += 1
# print("sum is", sum)

# #While loops
# i = 1
# sum = 0

# while sum < 10000:
#     sum = sum + i
#     i += 1

# #convert to for loops

# sum = 0 
# for i in range (10000):
#     sum = sum + i

# count = 5
# while count < n:
#     count += 1


# print("             Multiplication Table")
# print("  |", end = '')
# for j in range (1, 10):
#     print("  ", j, end = '')
# print()
# print("------------------------------------------------------")

# for i in range(1, 10):
#     print(i, "|", end = '')
#     for j in range(1, 10):

#         print(format(i*j, "4d"), end ='')
#     print()
    
    
# import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.bgcolor("lightpink")

# # Create a turtle
# flower = turtle.Turtle()
# flower.speed(0)
# flower.color("yellow")
# flower.width(2)

# # Draw a heart
# def draw_heart():
#     flower.begin_fill()
#     flower.left(140)
#     flower.forward(180)
#     flower.circle(-90, 200)
#     flower.left(120)
#     flower.circle(-90, 200)
#     flower.forward(180)
#     flower.end_fill()

# # Draw a petal
# def draw_petal():
#     flower.begin_fill()
#     flower.left(45)
#     flower.forward(100)
#     flower.left(45)
#     flower.forward(50)
#     flower.left(135)
#     flower.forward(100)
#     flower.left(45)
#     flower.forward(50)
#     flower.end_fill()
#     flower.left(90)

# # Draw flower petals
# flower.penup()
# flower.goto(0, -100)
# flower.pendown()
# flower.color("red")
# for _ in range(12):
#     draw_petal()
#     flower.left(30)

# # Draw the heart in the center
# flower.penup()
# flower.goto(0, -50)
# flower.pendown()
# flower.color("red")
# draw_heart()

# # Hide the turtle and display the drawing
# flower.hideturtle()
# turtle.done()


# import turtle

# # Set up the screen
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.title("Circle Drawing")

# # Set up the turtle
# t = turtle.Turtle()
# t.speed(2)  # Set the fastest drawing speed

# # Draw 10 circles
# radius = 5  # Initial radius
# for i in range(5):
#     t.penup()
#     t.goto(0, -radius)  # Start at (0, -radius)

#     t.pendown()
#     t.circle(radius)  # Draw the circle

#     # Increase the radius for the next circle
#     radius += 20

# # Hide the turtle
# #t.hideturtle()

# # Keep the window open
# turtle.done()


import turtle
#Set up the turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Triangle Drawing")

t = turtle.Turtle()
t.speed(0)  # Set the turtle speed to the fastest

# Draw 5 triangles
for i in range(5):
    side_length = 50 * (i + 1)  # Increase the side length for each triangle
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.penup()
    t.goto(-side_length / 2, -side_length * 3**0.5 / 6)  # Move to the next triangle position
    t.pendown()

# Hide the turtle and display the result
#t.hideturtle()
screen.mainloop()
turtle.done()
