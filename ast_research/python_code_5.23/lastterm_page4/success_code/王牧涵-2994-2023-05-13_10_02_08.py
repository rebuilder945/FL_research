sum=input().split(",")
n,m=input().split(",")
n=int(n)
m=int(m)
list1=[]
   
for x in sum:
    list1.append(x)
    if n>len(list1):
        print("error")
    if n<=len(list1): 
       a=sum[n]
    for i in range(m):
        list1.append(a)   
    ist1=[int(b) for b in list1]     
    print(list1) 
