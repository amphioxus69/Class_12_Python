import time
import sys

def cube(s):
    return (s*s*s)
def cuboid(l,w,h):
    return (l*w*h)
def sphere(r):
    return ((4/3)*(22/7)*(r**3))
def cylinder(r,h):
    return ((22/7)*(r**2)*h)
def cone(r,h):
    return (((22/7)*(r**2)*h)/3)
def pyramid(l,w,h):
    return ((l*w*h)/3)
def repeat():
    while True:
        choice = input("\nCalculate more volumes?(Yes(Y)/No(N)): ")
        if choice in "Yy":
            return True
        elif choice in "Nn":
            return False
        else:
            print("\n[[[INVALID INPUT, PLEASE TRY AGAIN]]]\n")
            continue
def ani_print(text,delay=0.1):
    for i in text:
        print(i,end='',flush=True)
        time.sleep(delay)
    

time.sleep(1)

for i in "VOLUME CALCULATOR":
    time.sleep(0.08)
    print(i,end='',flush=True)

for i in "\n=================\n":
    time.sleep(0.08)
    print(i,end='',flush=True)


while True:
    time.sleep(1)
    ani_print("\nCHOOSE FIGURE:-\n")
    time.sleep(1)
    print("1) Cube")
    time.sleep(0.5)
    print("2) Cuboid")
    time.sleep(0.5)
    print("3) Sphere")
    time.sleep(0.5)
    print("4) Cylinder")
    time.sleep(0.5)
    print("5) Cone")
    time.sleep(0.5)
    print("6) Pyramid")
    time.sleep(0.5)
    print("x) End Program")
    time.sleep(1)
    choice = input("Enter: ")
    match choice:
        case 'x':
            time.sleep(0.5)
            ani_print("\n[[[PROGRAM TERMINATED]]]\n")
            time.sleep(1)
            print()
            sys.exit(0)
        case '1':
            time.sleep(1)
            ani_print("\n[Cube]\n",delay=0.1)
            time.sleep(1)
            side = int(input("\nEnter side: "))
            time.sleep(1)
            ani_print("calculating.....")
            time.sleep(1)
            ani_print(f"\n\n[[[Volume of cube = {round(cube(side),2)}]]]\n")
            time.sleep(2.5)
            if repeat():
                time.sleep(0.5)
                ani_print("\n========================================\n",delay=0.03)
                continue
            else:
                time.sleep(1)
                ani_print("\n[[[Thank You]]]\n")
                time.sleep(1)
                print()
                break

        case '2':
            time.sleep(1)
            ani_print("\n[Cuboid]\n",delay=0.1)
            time.sleep(1)
            length = int(input("\nEnter length: "))
            width = int(input("Enter width: "))
            height = int(input("Enter height: "))
            time.sleep(1)
            ani_print("calculating.....")
            time.sleep(1)
            ani_print(f"\n\n[[[Volume of cuboid = {round(cuboid(length,width,height),2)}]]]\n")
            time.sleep(2.5)
            if repeat():
                time.sleep(0.5)
                ani_print("\n========================================\n",delay=0.03)
                continue
            else:
                time.sleep(1)
                ani_print("\n[[[Thank You]]]\n")
                time.sleep(1)
                print()
                break
        case '3': 
            time.sleep(1)
            ani_print("\n[Sphere]\n",delay=0.1)
            time.sleep(1)
            radius = int(input("\nEnter radius: "))
            time.sleep(1)
            ani_print("calculating.....")
            time.sleep(1)
            ani_print(f"\n\n[[[Volume of sphere = {round(sphere(radius),2)}]]]\n")
            time.sleep(2.5)
            if repeat():
                time.sleep(0.5)
                ani_print("\n========================================\n",delay=0.03)
                continue
            else:
                time.sleep(1)
                ani_print("\n[[[Thank You]]]\n")
                time.sleep(1)
                print()
                break
        case '4':
            time.sleep(1)
            ani_print("\n[Cylinder]\n",delay=0.1)
            time.sleep(1)
            radius = int(input("\nEnter radius: "))
            height = int(input("Enter height: "))
            time.sleep(1)
            ani_print("calculating.....")
            time.sleep(1)
            ani_print(f"\n\n[[[Volume of cylinder = {round(cylinder(radius,height),2)}]]]\n")
            time.sleep(2.5)
            if repeat():
                time.sleep(0.5)
                ani_print("\n========================================\n",delay=0.03)
                continue
            else:
                time.sleep(1)
                ani_print("\n[[[Thank You]]]\n")
                time.sleep(1)
                print()
                break
        case '5':
            time.sleep(1)
            ani_print("\n[Cone]\n",delay=0.1)
            time.sleep(1)
            radius = int(input("\nEnter radius: "))
            height = int(input("Enter height: "))
            time.sleep(1)
            ani_print("calculating.....")
            time.sleep(1)
            ani_print(f"\n\n[[[Volume of cone = {round(cone(radius,height),2)}]]]\n")
            time.sleep(2.5)
            if repeat():
                time.sleep(0.5)
                ani_print("\n========================================\n",delay=0.03)
                continue
            else:
                time.sleep(1)
                ani_print("\n[[[Thank You]]]\n")
                time.sleep(1)
                print()
                break
        case '6':
            time.sleep(1)
            ani_print("\n[Pyramid]\n",delay=0.1)
            time.sleep(1)
            base_length = int(input("\nEnter base length: "))
            base_width = int(input("Enter base width: "))
            base_height = int(input("Enter base height: "))
            time.sleep(1)
            ani_print("calculating.....")
            time.sleep(1)
            ani_print(f"\n\n[[[Volume of pyramid = {round(pyramid(base_length,base_width,base_height),2)}]]]\n")
            time.sleep(2.5)
            if repeat():
                time.sleep(0.5)
                ani_print("\n========================================\n",delay=0.03)
                continue
            else:
                time.sleep(1)
                ani_print("\n[[[Thank You]]]\n")
                time.sleep(1)
                print()
                break
        case _:
            time.sleep(1)
            ani_print("\n[[[INVALID INPUT, PLEASE TRY AGAIN]]]\n")
            continue