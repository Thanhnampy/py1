# Viết chương trình cho người dùng nhập vào kiểu dáng hình vẽ và màu sắc mong muốn. 
# Hình dáng: vuông hoặc tròn.
# Màu sắc: Vàng, đỏ và xanh dương.
# Sau đó in ra hình vẽ tương ứng
def hinhanh():
    import turtle
    shapeInput = input("Circle and square, what is your favorite shape: \r\n")
    if shapeInput == "circle" or shapeInput == "square":
        colorInput = input("what color will it be?, yellow, red or blue? \r\n")

        if colorInput == "yellow" or colorInput == "blue": 
            #setup cửa sổ terminal
                wn = turtle.Screen()
                wn.bgcolor("white")
                wn.title("Your shape")
            #hiển thị hình dạng shape
                displayShape = turtle.Turtle()
                displayShape.shape(shapeInput)
                displayShape.color(colorInput)
        else:
            print("This color not exist")
    else:
            print("This shape not exist")
    turtle.done()
if __name__=="__main__":
    hinhanh()




