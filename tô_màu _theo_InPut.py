def tomau():
    import turtle
    import random
    number = random.uniform(0,3) 
    intNumber = int(number)
    #setup terminal
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Circle") 
    #setup hình dạng khối tròn
    ball = turtle.Turtle()
    ball.shape("circle")
    if intNumber < 1:
        ball.color("green")
    elif intNumber < 2:
        ball.color("red")
    elif intNumber <3:
        ball.color("yellow")
    



    turtle.done()
if __name__=="__main__":
    tomau()
