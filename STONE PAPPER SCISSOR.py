import random
l=["STONE","PAPER","SCISSOR"]
print("Welcome ")
x = int(input("NO OF TURNS: "))
print("ENTER: (1 FOR STONE)\n(2 FOR PAPER)\n(3 FOR SCISSOR)")

u=0
c=0
i=1
while  (i<=x):
    print("User turn:")
    a= int(input())
    y=l[a-1]
    print("Computer Choosen: ")
    t=random.randrange(3)
    print(l[t])
    if y=="STONE" and (l[t]=="SCISSOR"):
        u+=1
    elif l[t]=="STONE" and ( y=="SCISSOR"):
        c+=1
    elif y=="SCISSOR" and l[t]=="PAPER" :
        u+=1
    elif l[t]=="SCISSOR" and y=="PAPER" :
        c+=1
    elif y=="PAPER" and l[t]=="STONE":
        u+=1
    elif l[t]=="PAPER" and y=="STONE":
        c+=1
    elif y==l[t]:
        print("TRY AGAIN")
    i+=1
print("USER: ",u , "   COMPUTER:",c)
if u>c:
    print("YOU WIN")
elif c>u :
    print("YOU LOSS")
else:
    print("GAME TIE")



