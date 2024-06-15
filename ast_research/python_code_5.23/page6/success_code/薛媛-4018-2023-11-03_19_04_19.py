def shift(lst):
    a=list(list1)
    c=len(a)-1
    b=a.copy()
    for i in range(c):
        b[i+1]=a[i]
    b[0]=a[c]
    return(b)
   
    

list1 = input().split(",") #输入格式 1,2,3,4,5
shift(list1)
print(list1)

