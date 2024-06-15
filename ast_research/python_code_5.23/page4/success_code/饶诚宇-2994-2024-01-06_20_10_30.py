lst=eval(input())
n,m=eval(input())
a=[]
lst=list(lst)
if n<=(len(lst)-1):
        b=lst[n]
        for i in range(m):
            a.append(b)
        print(lst+a)
else:
      print('error')
