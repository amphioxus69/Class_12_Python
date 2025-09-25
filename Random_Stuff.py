import random
import time

def generator(x,y):
    n = random.randint(x,y)
    return n

def ani_print(text,delay=0.05):
    for char in text:
        print(char,end='',flush=True)
        time.sleep(delay)
    print()

ani_print("Enter 2 numbers to set the range: ")
a = int(input("a = "))
b = int(input("b = "))
if a>b:
    a,b = b,a
x = generator((a+1),(b-1)) 
ani_print(f"Your random number is: {x}")