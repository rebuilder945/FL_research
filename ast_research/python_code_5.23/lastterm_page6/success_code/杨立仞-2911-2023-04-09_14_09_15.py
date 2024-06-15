a=input()
joker=""
for i in a:
    joker=str((int(i)+5)%10)+joker
print(joker)

