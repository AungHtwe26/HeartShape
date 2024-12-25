import turtle
import math

# Get user input for the text at the top of the heart
top_text = input("Enter the text to display at the top of the heart: ")

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("yellow")

def corazon(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * \
        math.cos(2*n) - 2*math.cos(3*n) - \
        math.cos(4*n)
    return x,y

t.penup()
for i in range(15):
    t.goto(0,0)
    t.pendown()
    for n in range(0, 100, 2):
        x,y = corazon(n/10)
        t.goto(x*i,y*i)
    t.penup()

# Add the user input text at the top of the heart
t.goto(0, 200)  # Adjust the position as needed
t.color("black")
t.write(top_text, align="center", font=("Arial", 24, "bold"))

# Add the text "I Love You" at the bottom of the heart
t.goto(0, -300)  # Adjust the position as needed
t.write("I Love You", align="center", font=("Arial", 24, "bold"))

t.hideturtle()
turtle.done()