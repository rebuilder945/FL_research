a=input()
b=[]
for i in range(int(a)):
    for j in range(2,int(a)):
        if i%j!=0:
            if int(a)==int(a.reverse()):
                b.append(i)
print(b)
