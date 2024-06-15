a=input()
joker=""
for i in a:
    joker=str((int(i)+5)%5)+joker
print(int(joker))

