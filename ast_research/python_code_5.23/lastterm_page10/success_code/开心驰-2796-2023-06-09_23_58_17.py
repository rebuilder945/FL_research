a=input()
b=0
for i in range(len(a)):
    if a[i].isdigit():
        count=1
        j=i
        while a[j+1].isdigit():
            count+=1
            j+=1
        if count>=b:
            b=count
            c=i
            d=j
print(a[c:d+1])
