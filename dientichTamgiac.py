def dientichtamgiac():
    import math
    # nhập giá trị 3 cạnh
    a = float(input("Nhap canh a:= "))
    b = float(input("Nhap canh b:= "))
    c = float(input("Nhap canh c:= "))

    if a+b>c or a+c>b or b+c>a:
        s = (a+b+c)/2   #chu vi tam giác
        Dientich = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"diện tích tam giác là: {Dientich} ")
    # thêm điều kiện kiểm tra 3 cạnh bất kỳ tạo thành tam giác hay không

if __name__=="__main__":
    dientichtamgiac()


