import turtle
import random

#ekran olustur
turtlebg=turtle.Screen()
turtlebg.bgcolor("pink")
turtlebg.title("Catch The Turtle")
turtle.setup(width=800,height=600)

#sınırlar
leftScreen=turtlebg.window_width()/2
rightScreen=turtlebg.window_width()/2
upScreen=turtlebg.window_height()/2
downScreen=turtlebg.window_height()/2

#turtle nesnesini olustur
catch_instance=turtle.Turtle()
catch_instance.shape("turtle")
catch_instance.shapesize(2)

movementTimer=0
while movementTimer <100:
    catch_instance.penup()
    movement=random.randint(1,50)
    catch_instance.forward(movement)
    angle=random.randint(-180,180)
    catch_instance.left(angle)

'''
x,y=catch_instance.position
if x> rightScreen or x< leftScreen or y > upScreen or y<downScreen:
    catch_instance.goto(random.randint())
    '''


turtle.done()


turtle.mainloop()
