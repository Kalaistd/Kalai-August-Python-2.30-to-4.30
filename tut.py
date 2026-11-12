# Example program, To draw the square
import turtle as t
z = t.Turtle() # Create turtle
z.shape("turtle") # Set turtle appearance
z.color("red")
z.fillcolor("green")
z.begin_fill() # First square
for i in range(4):
    z.forward(100)
    z.left(90)
z.end_fill()
z.penup() # Move to draw second square
z.backward(200)
z.pendown()

z.begin_fill()#second square
for i in range(4):
    z.forward(100)
    z.left(90)
z.end_fill()
z.penup() # Draw connector lines
z.backward(100)
z.pendown()
z.left(90)
z.forward(200)
z.right(90)
for i in range(2):# Draw large rectangle
    z.forward(500)
    z.right(90)
    z.forward(300)
    z.right(90)


z.penup() # Draw circle
z.goto(0, -150)
z.pendown()

z.fillcolor("purple")
z.begin_fill()
z.circle(50)
z.end_fill()

t.done() # Keep window open

