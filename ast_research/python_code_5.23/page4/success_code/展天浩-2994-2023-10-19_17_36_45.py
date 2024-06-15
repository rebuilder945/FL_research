list1=eval(input())
list1=list(list1)
m,n=eval(input())
if m>=len(list1):
    print("error")
else:
    x1=list1[m]
    while n>0:
        list1.append(int(x1))
        n-=1
print(list1)
                
