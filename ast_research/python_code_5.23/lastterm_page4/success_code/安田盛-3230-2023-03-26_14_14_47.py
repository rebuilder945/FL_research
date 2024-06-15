lst=eval(input())
lst.sort()
a=[]
for i in range(len(lst)):
    b=lst.pop()
    a.append(str(b))
c=a[0]
for x in a[1:]:
    c=c+x
print(int(c))
    



    
            


