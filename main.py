import turtle as turtle
import random

random_number = random.randrange(1,5)
done = False

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


while done == False:
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


  selection = input("\n1. Star\n2. Square\n3. Hexagon\n4. Triangle\n5. Random\n6. Exit\nSelect a number: ")

  if selection == "1":
    turtle.clear()
    print("Excellent choice! Go to the result tab to see your creation.")
    star()
    print("\nPick again!")

  elif selection == "2":
    turtle.clear()
    print("Excellent choice! Go to the result tab to see your creation.")
    square()
    print("\nPick again!")

  elif selection == "3":
    turtle.clear()
    print("Excellent choice! Go to the result tab to see your creation.")
    hexagon()
    print("\nPick again!")

  elif selection == "4":
    turtle.clear()
    print("Excellent choice! Go to the result tab to see your creation.")
    triangle()
    print("\nPick again!")

  elif selection == "5":
    turtle.clear()
    print("Random Shape, coming right up! Go to the result tab to see your creation.")
    random()
    print("\nPick again!")

  elif selection == "6":
    print("\nThanks for playing!\n")
    done = True
