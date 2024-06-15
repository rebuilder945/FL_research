a=listinput()
s=""
for i in a:
    s+=str((int(i)+5)%10)
print(s[::-1])

