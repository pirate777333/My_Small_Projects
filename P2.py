import random

dictionary={"Messi":"Barca",
            "CR7":"Juve",
            "KDB":"City",
            "Fernandes":"UTD",
            "Samba":"NFFC",
            "Britt":"Boro",
            "DeGea":"UTD",
            "Mount":"Chelsea",
            "JT":"No",
            "Drogba":"CIV"}

x=input("Player name: ")
l=[]
for k in dictionary:
    if x.lower() == k.lower():
        print(dictionary[k])
    else:
        l.append(k)

if len(dictionary)==len(l):
    print("Results not found")
elif len(dictionary)>len(l):
    print("Result successfully found")
