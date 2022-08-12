import random

import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)
turty = Turtle()
turty.hideturtle()
turty.color("cyan")
turty.speed(10000)
turty.penup()
turty.setposition(-435,-350)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
end = False


def draw_dot():
    for i in range(0, 22):
        color = random.choice(color_list)
        turty.dot(25, color)
        turty.fd(40)


def turtle_move():
    global end
    while end is False:
        draw_dot()
        for i in range(0, 2):
            turty.left(90)
            turty.fd(40)
        draw_dot()
        for i in range(0, 2):
            turty.right(90)
            turty.fd(40)
        break


while True:
    if round(turty.ycor()) > 290:
        end = True
        break
    turtle_move()
    print(round(turty.ycor()))

screen.exitonclick()