from turtle import color


def hcn():
    import turtle
    line = turtle.Turtle()
    line.pensize(4)
    line.speed(5)
    color = input("Nhập tên màu: ")
    a = float(input("Nhập chiều dài: "))
    b = float(input("Nhập chiều rộng: "))
   
    line.begin_fill()
    line.color(color)

    for i in range (2):
        line.forward(a)    # di lui``
        line.left(90)
        line.forward(b)     # di tien'
        line.left(90)

    line.end_fill()

    ChuviHCN = (a+b)*2
    print(f"chu vi HCN là: {ChuviHCN}")
    Dientich = a*b
    print(f"diện tích HCN là: {Dientich} ")


    turtle.done()
if __name__ == "__main__":
    hcn()
