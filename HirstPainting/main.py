# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     c = (r,g,b)
#     rgb_colors.append(c)
# print(rgb_colors)

import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()


color_list = [(248, 238, 219), (223, 155, 90), (214, 240, 228), (240, 206, 90), (104, 170, 203), (36, 109, 149), (199, 227, 239), (113, 193, 161), (153, 61, 94), (208, 78, 109), (243, 215, 226), (25, 134, 101), (224, 81, 59), (205, 133, 155), (184, 59, 43), (177, 166, 36), (138, 219, 198), (39, 54, 113), (238, 161, 180), (105, 40, 73), (137, 215, 228), (239, 168, 157), (14, 93, 69), (60, 166, 132), (27, 47, 88), (53, 157, 186), (109, 116, 170), (72, 36, 65), (14, 69, 51), (180, 186, 218)]
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(0,number_of_dots):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if (dot_count+1) % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()
