c=eval(input())
k=[x for x in c if c.count(x)==1]
k.sort()
if k!=[]:
   print(*k,sep=',')    #*k就是把列表中的元素提取出来，而且加逗号的split(',')只能用字符串，列表用sep=','
else:
   print(False)
