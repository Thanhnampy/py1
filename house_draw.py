from turtle import begin_fill, goto, pensize
import math
import random  
def house():
    import turtle
    line = turtle.Turtle()
    turtle.bgcolor("#994444") # đổi màu nền 
    line.pensize(4)
    line.speed(10)

    line.penup()
    line.fd(200) 
    line.pendown()
    
    
    line.penup()
    line.rt(90)
    line.fd(130)
    line.lt(90)
    line.pendown()
 
    #ve tang 1
    line.color("gray","#fff0f5")
    line.begin_fill()
    for i in range(4):
        line.rt(90)
        line.fd(200)
    line.end_fill()
    line.penup()
    line.rt(90)
    line.fd(200)
    line.pendown()
 


    #ve cua nha
    line.penup()
    line.rt(90)
    line.fd(70)
    line.pendown()
    
    line.begin_fill()
    line.color('brown')

    line.rt(90)
    line.fd(80)  
    line.lt(90)
    line.fd(60)
    line.lt(90)
    line.fd(80)
    line.lt(90)
    line.fd(60)
    line.end_fill()
    #ve mat ngang cua nha
    line.penup()    
    line.fd(70)    
    line.pendown()
    
    line.color("gray","#fff0f5") 
    line.begin_fill()
    line.lt(15)
    line.fd(300)
    line.lt(75)
    line.fd(200)
    line.lt(105)
    line.fd(300)
    line.lt(75)
    line.fd(200)

    line.rt(180)
    line.fd(200)
    line.end_fill()


    # ve tang 2
    line.color("gray","#fff0f5") 
    line.begin_fill()
    for i in range(4):
        line.fd(200)
        line.lt(90)

    line.rt(75)
    line.fd(300)
    line.lt(75)
    line.fd(200)
    line.lt(105)
    line.fd(300)
    line.end_fill()
    
     
    #Ve mai nha
    line.color('slategray',"#fff0f5")
    line.begin_fill()
    line.rt(75)
    line.fd(200)
    line.lt(120)
    line.fd(200)
    line.lt(120)
    line.fd(200)
    line.end_fill()

    line.color('slategray','slategray')
    line.begin_fill()
    line.lt(120)
    line.fd(200)
    line.rt(105)
    line.fd(300)
    line.rt(75)
    line.fd(200)
    line.rt(105)
    line.fd(300)
    line.end_fill()


    # ve cua so
    line.penup()
    line.lt(75)
    line.fd(25)
    line.pendown()
    line.rt(90)

    line.penup()
    line.fd(25)
    line.pendown()

    line.color("#8b0000","#ffa07a")
    line.begin_fill()
    for i in range(4):
        line.fd(25)
        line.lt(90)
    line.penup()    
    line.fd(25)    
    line.pendown()
    
    for i in range(4):
        line.fd(25)
        line.lt(90)

    line.penup()  
    line.lt(90)  
    line.fd(25)    
    line.pendown()    
    
    for i in range(4):
        line.fd(25)
        line.rt(90)

    for i in range(4):
        line.fd(25)
        line.lt(90)
    line.end_fill()

    
    line.penup()  
    line.lt(180)  
    line.fd(25)
    line.lt(90)
    line.fd(100)    
    line.pendown() 

    line.color("#8b0000","#ffa07a")
    line.begin_fill()
    for i in range(4):
        line.fd(25)
        line.lt(90)
    line.lt(180)
    for i in range(4):
        line.fd(25)
        line.rt(90)

    line.penup()  
    line.rt(90)  
    line.fd(25)    
    line.pendown() 
    
    for i in range(4):
        line.fd(25)
        line.rt(90)
    for i in range(4):
        line.fd(25)
        line.lt(90)
    line.end_fill()


    line.penup()  
    line.lt(90)  
    line.fd(150) 
    line.rt(90)
    line.fd(175) 
    line.rt(90)
    line.fd(25)  
    line.pendown() 

    '''
    '''

    line.color("#8b0000","#ffa07a")
    line.begin_fill()
    for i in range(4):
        line.fd(25)
        line.lt(90)
    line.penup()    
    line.fd(25)    
    line.pendown()
    
    for i in range(4):
        line.fd(25)
        line.lt(90)

    line.penup()  
    line.lt(90)  
    line.fd(25)    
    line.pendown()    
    
    for i in range(4):
        line.fd(25)
        line.rt(90)

    for i in range(4):
        line.fd(25)
        line.lt(90)
    line.end_fill()

    
    line.penup()  
    line.lt(180)  
    line.fd(25)
    line.lt(90)
    line.fd(100)    
    line.pendown() 

    line.color("#8b0000","#ffa07a")
    line.begin_fill()
    for i in range(4):
        line.fd(25)
        line.lt(90)
    line.lt(180)
    for i in range(4):
        line.fd(25)
        line.rt(90)

    line.penup()  
    line.rt(90)  
    line.fd(25)    
    line.pendown() 
    
    for i in range(4):
        line.fd(25)
        line.rt(90)
    for i in range(4):
        line.fd(25)
        line.lt(90)
    line.end_fill()

    # lam num van cua
    line.penup() 
    line.fd(150) 
    line.lt(90)  
    line.fd(25) 
    line.lt(90)  
    line.fd(40) 
    line.pendown() 
    line.color("midnightblue")
    line.dot(10)

    '''
    '''
    # the Sun
    line.penup()      
    line.fd(600) 
    line.lt(90)  
    line.fd(600) 
    line.pendown() 
    line.color('yellow', 'orange')
    line.pensize(2)
    line.begin_fill()
    for i in range(69):
        line.fd(100)
        line.lt(170)
    line.end_fill()
    
    
    #vẽ cây
    line.penup()
    line.home()
    line.goto(-150,-150)    
    line.pendown()
    line.lt(90)
    line.pensize(1)
    line.color("greenyellow","olivedrab")
    line.begin_fill()
    line.circle(50)
    line.end_fill()
        #vẽ than cây
    line.penup()
    line.lt(90)
    line.fd(50)
    line.lt(90)
    line.fd(55)
    line.pendown()  
    line.pencolor("black")
    line.pensize(10)
    line.color("saddlebrown") 
    line.fd(100)
       

    turtle.done() 
if __name__ == "__main__":
    house()