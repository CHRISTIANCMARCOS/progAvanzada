import turtle
ventana = turtle.Screen()
ventana.bgcolor('white')
ventana.title('Mi ventana')

rafael = turtle.Turtle()
rafael.shape("turtle")
rafael.color("black")
rafael.pensize(4)
rafael.speed(1000)
rafael.penup()
rafael.setpos(-400,-200)

i = 1
rafael.pendown()
while i <= 6:

    rafael.color("yellow")
    rafael.pendown()
    rafael.left(30)
    rafael.forward(50)
    rafael.left(120)
    rafael.forward(50)
    rafael.left(120)
    rafael.forward(50)
    rafael.left(150)
 
    i = i + 1

rafael.penup()
rafael.forward(200)


i = 1
rafael.pendown()
while i <= 6:

    rafael.color("yellow")
    rafael.pendown()
    rafael.left(30)
    rafael.forward(50)
    rafael.left(120)
    rafael.forward(50)
    rafael.left(120)
    rafael.forward(50)
    rafael.left(150)
 
    i = i + 1

rafael.left(180)
rafael.color("orange")
rafael.forward(100)
rafael.right(60)
rafael.forward(100)
rafael.left(120)
rafael.forward(100)
rafael.left(120)
rafael.penup()
rafael.forward(100)
rafael.pendown()
rafael.left(60)
rafael.forward(100)
rafael.right(120)
rafael.forward(100)
rafael.right(180)
rafael.forward(100)
rafael.left(60)
rafael.forward(100)
rafael.right(140)
rafael.color("red")
rafael.forward(50)
rafael.right(130)
rafael.penup()
rafael.forward(30)
rafael.left(90)
rafael.forward(60)
rafael.pendown()
rafael.left(40)
rafael.forward(50)
rafael.left(140)
rafael.forward(35)

rafael.penup()
rafael.setpos(-240,250)

n = 1
while n <= 3:

    i = 1
    rafael.pendown()
    while i <= 6:

        rafael.color("cyan")
        rafael.pendown()
        rafael.left(30)
        rafael.forward(30)
        rafael.left(120)
        rafael.forward(30)
        rafael.left(120)
        rafael.forward(30)
        rafael.left(150)
 
        i = i + 1

    n = n + 1
    rafael.penup()
    rafael.forward(130) 

rafael.left(180)
rafael.penup()
rafael.forward(325) 
rafael.right(90)
rafael.forward(70) 
rafael.right(90)

n = 1
while n <= 3:

    i = 1
    rafael.pendown()
    while i <= 6:

        rafael.color("cyan")
        rafael.pendown()
        rafael.left(30)
        rafael.forward(30)
        rafael.left(120)
        rafael.forward(30)
        rafael.left(120)
        rafael.forward(30)
        rafael.left(150)
 
        i = i + 1

    n = n + 1
    rafael.penup()
    rafael.forward(130) 

rafael.penup()
rafael.left(180)
rafael.forward(600) 

rafael.right(90)
rafael.forward(430) 
rafael.pendown()
rafael.color("green")
rafael.right(90)
rafael.forward(400) 
rafael.right(180)
rafael.forward(800) 
rafael.right(180)
rafael.forward(300)
rafael.right(90)
rafael.penup()
rafael.forward(140)
rafael.left(90)
rafael.forward(130)
rafael.left(80)

i = 1
rafael.pendown()
while i <= 6:

    rafael.color("green")
    rafael.pendown()
    rafael.left(30)
    rafael.forward(50)
    rafael.left(120)
    rafael.forward(50)
    rafael.left(120)
    rafael.forward(50)
    rafael.left(150)
 
    i = i + 1

rafael.penup()
rafael.left(190)
rafael.forward(100)
rafael.left(50)

i = 1
rafael.pendown()
while i <= 6:

    rafael.color("green")
    rafael.pendown()
    rafael.left(30)
    rafael.forward(50)
    rafael.left(120)
    rafael.forward(50)
    rafael.left(120)
    rafael.forward(50)
    rafael.left(150)
 
    i = i + 1

rafael.penup()
rafael.right(140)
rafael.forward(100)
rafael.left(90)
rafael.forward(110)
rafael.left(30)

i = 1
rafael.pendown()
while i <= 6:

    rafael.color("green")
    rafael.pendown()
    rafael.left(30)
    rafael.forward(80)
    rafael.left(120)
    rafael.forward(80)
    rafael.left(120)
    rafael.forward(80)
    rafael.left(150)
 
    i = i + 1

rafael.penup()
rafael.right(120)
rafael.right(90)
rafael.forward(80)
rafael.color("brown")
rafael.pendown()
rafael.forward(267)
rafael.left(180)
rafael.forward(120)
rafael.left(80)
rafael.forward(55)
rafael.penup()
rafael.right(80)
rafael.forward(100)
rafael.right(100)
rafael.pendown()
rafael.forward(55)
rafael.penup()
rafael.forward(55)

ventana.mainloop()




