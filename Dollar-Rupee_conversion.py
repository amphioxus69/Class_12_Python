def convert_void_d(price):
    x = price*80
    print(f'{price} dollars = {x} rupees')
def convert_void_rs(price):
    x = price/80
    print(f'{price} rupees = {x} dollars')
def convert_nonvoid_d(price):
    return (price*80)
def convert_nonvoid_rs(price):
    return (price/80)
    
print(r"DOLLAR/RUPEE CONVERSION")
print(r"=======================")

while True:
    choice = int(input("Choose mode:\n1) DOLLAR to RUPEE\n2) RUPEE to DOLLAR\nEnter: "))
    match choice:
        case 1:
            price = int(input("Enter the price in dollars: "))
            while True:
                choice = int(input("1)Void\n2)Non-Void\nENTER: "))
                match choice:
                    case 1: 
                        convert_void_d(price)
                        break
                    case 2:
                        in_rupees = convert_nonvoid_d(price)
                        print(f'{price} dollars = {in_rupees} rupees')
                        break
                    case _:
                        print("TRY AGAIN")
                        continue
            break
        case 2:
            price = int(input("Enter the price in rupees: "))
            while True:
                choice = int(input("1)Void\n2)Non-Void\nENTER: "))
                match choice:
                    case 1: 
                        convert_void_rs(price)
                        break
                    case 2:
                        in_dollars = convert_nonvoid_rs(price)
                        print(f'{price} dollars = {in_dollars} rupees')
                        break
                    case _:
                        print("TRY AGAIN")
                        continue
            break
        case _:
            print("TRY AGAIN, WRONG INPUT")
