import random

listofwords=['Antilopa','Slon','Mrav','Hipopotamus','Mrvojed','Dikobraz',
             'Glavata Želva','Bodljikavo prase','Ljenjivac','Zmija','Pas']
x=random.randint(0,len(listofwords))
#print(listofwords[x])

rijec=listofwords[x-1]
#print('_ '*len(rijec))
pokusaja=5
listofletters=list(rijec.lower())
#print(listofletters)
l=[]
for i in range(len(listofletters)):
    l.append('_ ')

for i,j in enumerate(listofletters):
    if j==' ':
        l[i]=' '
        
print(l)    
slova=[]
while pokusaja !=0:
    slovo=input("Slovo: ")
    if slovo in slova:
        print("Already Used...")
    else:
        slova.append(slovo)
        for i,j in enumerate(listofletters):
            if j.lower()==slovo.lower():
                l[i]=slovo.lower()
        if slovo.lower() not in listofletters:
            pokusaja=pokusaja-1
        if '_ ' not in l:
            print('You Won!')
            print(l)
            break
        if pokusaja==0:
            print("You Lost!")
            print(listofletters)
    print(l)
    print("Pokušaja ",pokusaja)

    
