def chanle():
    a = int(input("Nhap so bat ki: "))
    if a % 2 == 0:
        print(f"{a} là số chẵn")
    else:
        print(f"{a} là số lẻ")

if __name__=="__main__":
    chanle()