def dientichHTron():
    import math
    # nhập giá trị 3 cạnh
    r = float(input("Nhap canh a:= "))
    pi = math.pi  
    Dientich = pi*(r**2)
    print(f"diện tích hình vuông là: {Dientich} ")

if __name__=="__main__":
    dientichHTron()