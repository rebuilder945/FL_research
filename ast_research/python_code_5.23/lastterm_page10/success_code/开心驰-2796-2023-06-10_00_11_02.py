a=input()
b=0
for i in range(len(a)):
        count=0
        j=i
        while a[j].isdigit():
            count+=1
            if j<len(a)-1:
                j+=1
            else:
                break    
        if count>=b:
            b=count
            c=i
            d=j
if a[len(a)-1].digit():
     print(a[c:d+1])
else:
     print(a[c:d])
