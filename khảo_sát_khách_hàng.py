def KhaosatKH():
    bill = float(input("Nhập bill: "))
    if bill >= 150:
        price = bill - 50
        print("Discount 50 USD")
        print(f"Phải trả {price}")
    elif bill >= 100:
        price = bill - 25
        print("Discount 25 USD")
        print(f"Phải trả {price}")
    elif bill >= 75:
        price = bill - 15
        print("Discount 15 USD ")
        print(f"Phải trả {price}")
    else: 
        price = bill
        print("No discount") 
        print(f"Phải trả {price}")   
if __name__ == "__main__":
    KhaosatKH() 
    
