def vematcuoi():
    import turtle
    line = turtle.Turtle()
    line.pensize(5)
    line.speed(10)
    line.color("blue","bisque")

    #Vẽ khuôn mặt
    facesize = 200
    line.penup()
    line.goto(0, -200)
    line.pendown()
    line.begin_fill()
    line.circle(facesize)
    line.end_fill()
    
    #Vẽ đôi mắt
    line.color("red","yellow")
    line.begin_fill()
    line.penup()
    line.goto(-100,50)
    line.pendown()

    #khai báo eyesight
    eye_sight = 15
    line.circle(eye_sight)
    line.end_fill()

    line.penup()
    line.goto(100, 50)
    line.pendown()

    line.begin_fill()
    line.circle(eye_sight)
    line.end_fill()

    #vẽ mũi
    line.penup ()
    line.goto(0,50)
    line.pendown()

    line.color("brown", "pink")
    line.begin_fill()
    line.circle(-40, steps=3)
    line.end_fill()

    #vẽ nụ cười
    line.penup ()
    line.goto(-100,-70)
    line.pendown()
    line.color("pink","darksalmon")
    line.begin_fill()
    line.rt(90)
    line.circle(100,180)
    line.lt(90)
    line.fd(200)
    line.end_fill()


    turtle.done()
if __name__=="__main__":
    vematcuoi()