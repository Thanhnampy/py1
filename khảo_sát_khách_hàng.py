def KhaosatKH():
    tongBill = float(input("Nhập bill: "))
    if tongBill >= 150:
        price = tongBill - 50
        print("Discount 50 USD")
        print(f"Phải trả {price}")
    elif tongBill >= 100:
        price = tongBill - 25
        print("Discount 25 USD")
        print(f"Phải trả {price}")
    elif tongBill >= 75:
        price = tongBill - 15
        print("Discount 15 USD ")
        print(f"Phải trả {price}")
    elif tongBill < 75: 
        price = tongBill
        print("No discount") 
        print(f"Phải trả {price}")   
if __name__ == "__main__":
    KhaosatKH() 
    