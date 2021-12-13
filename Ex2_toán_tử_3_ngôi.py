def timMax():
    a = int(input("Nhap so a bat ky: "))
    b = int(input("Nhap so b bat ky: "))
    c = int(input("Nhap so c bat ky: "))
    max = a if a > b and a>c else b if b>c else c
    print(f"Max = {max}")
if __name__=="__main__":    
    timMax()
