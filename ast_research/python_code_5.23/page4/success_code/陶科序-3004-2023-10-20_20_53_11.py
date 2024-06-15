a = input()
b = []
for i in a :
    for j in range(2,int(i)):
        if int(i)%j == 0:
            pass
    else:
        b.append(i)
print(b)


