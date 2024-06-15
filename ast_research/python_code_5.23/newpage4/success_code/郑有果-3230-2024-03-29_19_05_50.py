m=eval(input())
lst=list(m)
lst.sort(reverse=True)
if lst[0]==0:
   print("0")
else:
    for x in lst:
        print(x,end="")


