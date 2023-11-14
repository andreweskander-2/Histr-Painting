#importing all the needed modules
import turtle
import random
import colorgram
import turtle as t

#defining the required variables
screen_up = t.Screen()
tim = t.Turtle()
turtle.colormode(255)
tim.speed(0)
tim.penup()
color_list = []
y = 0

#a function to extract colors from a picture using the colorgram module
def color_extract():
    colors = colorgram.extract('painting.jpg', 20)
    i = 0
    for color in colors:
        color_list.append(colors[i].rgb)
        i += 1

#a function to draw a straight line of 5x dots
def line_of_dots():
    for i in range(4):
        tim.dot(15, color_list[random.randint(0,19)])
        tim.forward(50)
        tim.dot(15, color_list[random.randint(0, 19)])

#a function to move the cursor up by one line and start from x = 0
def move_up(y_pos):
    tim.goto(0,y_pos)

#the code to run all the functions together to draw a square with 5 lines each line with 5 dots
color_extract()
for z in range(5):
    line_of_dots()
    y += 50
    move_up(y)

screen_up.exitonclick()
