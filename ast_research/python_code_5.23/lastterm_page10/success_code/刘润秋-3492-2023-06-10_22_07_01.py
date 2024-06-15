n=input()
lst=[]
for x in n:
    a=n.count(x)
    if a == 1:
        lst.append(x)
if len(n)>=1:
    print(lst[0])
elif len(n)==0:
   print("None")
