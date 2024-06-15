a = input().split(',')
b = []
for i in a :
    for j in range(1,i+1):
        if i%j ==0:
            pass
        else:
            b.append(i)
print(b)


