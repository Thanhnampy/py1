def tinhBMI():
    import math
    weight = float(input("Nhap so can nang cua ban: "))
    height = float(input("Nhap chieu cao cua ban: "))
    BMI = weight / (height ** 2)
    if BMI > 40:
        print("Beo phi cap do 3")
    elif 35 <= BMI < 40:
        print("Beo phi cap do 2")
    elif 30 <= BMI < 35:
        print("Beo phi cap do 1")
    elif 35 <= BMI < 30:
        print("Thua can")
    elif 18.5 <= BMI < 25:
        print("Binh thuong")
    elif 17 <= BMI < 18.5:
        print("Gay cap do 1")
    elif 16 <= BMI < 17:
        print("Gay cap do 2")
    elif BMI < 16:
        print("Gay cap do 3")

if __name__ == "__main__":
    tinhBMI()