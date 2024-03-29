import turtle

# Kalbi çizmek için fonksiyon
def draw_heart():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.begin_fill()
    t.color("red")
    t.left(140)
    t.forward(224)
    for i in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for i in range(200):
        t.right(1)
        t.forward(2)
    t.forward(224)
    t.end_fill()
    t.penup()
    t.goto(0, 0)
    t.color("white")
    t.write("Takip Etmeyi Unutmayın !", align="center", font=("Arial", 20, "normal"))
    t.goto(0, -30)  # Yeni bir satır eklemek için yeni bir konuma git
    t.write("@javakadir", align="center", font=("Arial", 20, "normal"))
    t.hideturtle()

# Ana program
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
draw_heart()
turtle.done()
