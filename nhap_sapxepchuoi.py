def xuLyChuoi():
    items = [x for x in input('Nhap vao mot chuoi: ')]
    print('truoc khi sap xep \r\n')
    for a in items:
        print(a)
    items.sort()
    print('sau khi sap xep \r\n')
    for a in items:
        print(a)
    print('_'.join(items))
if __name__=="__main__":
    xuLyChuoi()
