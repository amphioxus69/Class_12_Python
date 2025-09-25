import time
import math

def ani_print(text,delay=0.05):
    for i in text:
        print(i,end='',flush=True)
        time.sleep(delay)
    print()

def power(x,n=2):
    ans = math.pow(x,(1/n))
    return ans

ani_print("For x root n :")
x = int(input("x = "))
n = int(input("n = "))

ans = power(x,n)

ani_print(f"{x} root {n} = {round(ans,2)}")