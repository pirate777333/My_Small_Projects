import random

a=input("Y to do roll, Q to quit  ")
while a.lower()!="q":
    if a.lower()=="y":
        print("0"*random.randint(1,6))
    elif a.lower()=="q":
        break
    else:
        print("idk...")
    a=input("Y to do roll, Q to quit  ")
quit
