import turtle as turtle
import random

random_number = random.randrange(1,5)

print("Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!")

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()

def star():
  turtle.pencolor("purple")
  for i in range(0,5):
    turtle.forward(110)
    turtle.right(216)

def square():
  turtle.pencolor("orange")
  for i in range(0,4):
      turtle.forward(100)
      turtle.right(90)

def hexagon():
  turtle.pencolor("red")
  for i in range(0,6):
    turtle.forward(100)
    turtle.right(60)

def triangle():
  turtle.pencolor("green")
  for i in range(0,3):
    turtle.forward(110)
    turtle.right(120)

def random():
  turtle.pencolor("black")
  if random_number == 1:
    star()
  elif random_number == 2:
    square()
  elif random_number == 3:
    hexagon()
  elif random_number == 4:
    triangle()


selection = input("1. Star\n2. Square\n3. Hexagon\n4. Triangle\n5. Random\nSelect a number: ")
if selection == "1":
  print("Excellent choice! Go to the result tab to see your creation.")
  star()
elif selection == "2":
  print("Excellent choice! Go to the result tab to see your creation.")
  square()
elif selection == "3":
  print("Excellent choice! Go to the result tab to see your creation.")
  hexagon()
elif selection == "4":
  print("Excellent choice! Go to the result tab to see your creation.")
  triangle()
elif selection == "5":
  print("Random Shape, coming right up! Go to the result tab to see your creation.")
  print(random_number)
  random()
