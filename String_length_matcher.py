import time

def length_checker(a,b):
    if len(a)==len(b):
        return True
    else:
        return False
    
def ani_print(text,delay=0.05):
    for i in text:
        print(i,end='',flush=True)
        time.sleep(delay)
    print()

ani_print("Enter 2 strings: ")
a = input("a = ")
b = input("b = ")
if length_checker(a,b):
    ani_print("Yes, same size strings")
else:
    ani_print("No, different sized strings")
