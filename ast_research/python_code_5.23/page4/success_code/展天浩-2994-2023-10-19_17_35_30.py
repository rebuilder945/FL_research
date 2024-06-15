list1=eval(input())
list1=list(list1)
m,n=eval(input())
if m-1>len(list1):
    print("Error")
else:
    x1=list1[m]
    while n>0:
        list1.append(int(x1))
        n-=1
print(list1)
                
