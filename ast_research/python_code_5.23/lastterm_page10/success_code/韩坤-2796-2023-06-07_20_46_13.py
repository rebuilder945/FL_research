n=input()
for x in n:
    if x.isalpha():
        n=n.replace(x," ")
if n==" "*len(n):
    print("No digits")
else:
    lst=n.split()
    lst1=sorted(lst,key=lambda x:len(x),reverse=True)
    a=len(lst1[0])
    lst2=[eval(x) for x in lst1 if len(x)==a]

    print(lst2[-1])

