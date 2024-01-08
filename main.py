import turtle
import random

#ekran olustur
turtlebg=turtle.Screen()
turtlebg.bgcolor("pink")
turtlebg.title("Catch The Turtle")

#turtle
catch_instance=turtle.Turtle()
catch_instance.shape("turtle")
catch_instance.shapesize(2)
catch_instance.penup()


score=0


#skor yazısı
score_turtle=turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0,250)
score_turtle.write("Skor:0", align="center",font=("Arial",16,"normal"))

#countdown yazısı
countdown_turtle=turtle.Turtle()
countdown_turtle.hideturtle()
countdown_turtle.color("black")
countdown_turtle.penup()
countdown_turtle.goto(0,200)

click_allowed=True

#skoru yukseltme
def increase_score(x,y):
    global score, click_allowed
    if click_allowed:
        score+=1
        score_turtle.clear()
        score_turtle.write(f"Skor: {score}",align="center",font=("Arial",24,"normal"))
        click_allowed=False
        turtlebg.ontimer(reset_click,1000)

#reset click
def reset_click():
    global click_allowed
    click_allowed=True

#skor yukseltme
catch_instance.onclick(increase_score)

#ışınlanma
def teleport_turtle():
    catch_instance.hideturtle()
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    catch_instance.goto(x, y)
    catch_instance.showturtle()
    turtlebg.ontimer(teleport_turtle, 500)

def countdown_timer(count):
     countdown_turtle.clear()
     if count>0:
         countdown_turtle.write(f"Kalan Süre: {count} saniye", align="center", font=("Arial", 24, "normal"))
         turtlebg.ontimer(lambda: countdown_timer(count - 1), 1000)
     else:
         countdown_turtle.clear()
         countdown_turtle.write("Süre Doldu!", align="center", font=("Arial", 24, "normal"))
         turtlebg.ontimer(stop_game, 2000)  # Oyunu 2 saniye sonra kapat


def stop_game():
    turtle.done()


countdown_timer(20)


teleport_turtle()
turtle.mainloop()
