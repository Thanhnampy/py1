'''
Ve hinh vuong
'''

# import turtle
# def square():
#     #khoi tao thu vien
#     import turtle
#     #khoi tao bien
#     line = turtle.Turtle()
#     line.color("red")

#     #lap 4 lan di chuyen
#     for i in range (4):
#         line.forward(100)       #di thang 100 pixel
#         line.right(90)          #quay phai 90 do

#     turtle.done()
# if __name__ == "__main__":
#     square()    

'''
Ve hinh chu nhat
'''
def hcn():
    import turtle
    line = turtle.Turtle()
    line.pensize(4)
    line.speed(5)
    line.color("red","yellow")
    a = 300     #chieu dai hcn
    b = 150     #chieu rong hcn
   
    line.begin_fill()

    line.circle(100)
    line.penup()
    line.forward(100)     # lệnh nhảy
    line.pendown()

    for i in range (2):
        line.forward(a)    # di lui``
        line.left(90)
        line.forward(b)     # di tien'
        line.left(90)

    line.penup()
    line.forward(-200)     # lệnh nhảy
    line.pendown()

    for i in range (4):
        line.forward(-b)       #di thang 100 pixel
        line.right(90)          #quay phai 90 do

    line.end_fill()
    turtle.done()
if __name__ == "__main__":
    hcn()

'''
hinh tron`
'''
# import turtle
# t=turtle.Turtle()
# t.pensize(5)
# #đặt màu sắc cho viền hình tròn là màu đỏ
# t.pencolor("red")
# #đặt màu nền cho hình tròn là màu xanh
# t.fillcolor("green")
# t.begin_fill()
# #đặt bán kính của hình tròn là 100
# t.circle(100)
# t.end_fill()
# turtle.done()
