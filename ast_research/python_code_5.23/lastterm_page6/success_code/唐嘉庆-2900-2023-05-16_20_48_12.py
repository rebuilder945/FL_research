n=eval(input())
if n%1!=0 or n<=1:
    print("illegal input")
else:
    lst=[]
    for i in range(n):
       if str(i)==str(i)[::-1]:
            lst.append(i)
    del lst[0:2]
    jack=lst.copy()

    for x in lst:
      for i in range(2,x):
          if x%i==0:
             jack.remove(x)
             break
    print(" ".join (str(i) for i in jack))
