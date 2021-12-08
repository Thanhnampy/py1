# xét chuỗi 1 có là con của chuỗi 2 hay không
def nhapdata():
    chuoi1 = input("Nhap vao chuoi 1: ")
    chuoi2 = input("Nhap vao chuoi 2: ")
    if chuoi1 in chuoi2:
        print("True")
    else:
        print("False")
    print("độ dài chuỗi 1 là: " + str(len(chuoi1)))
    if chuoi1 not in chuoi2:
        print("not in")
    else:
        print("in")
    print(len(chuoi1)) #độ dài chuỗi 1
    print(len(chuoi2)) #độ dài chuỗi 2

if __name__=="__main__":
    nhapdata()
