ls=eval(input())
a,b=eval(input())
if a<len(ls)-1 and b<=len(ls)-1 and a<=b:
    for i in range(a,b):
        ls.pop(i) 
    print(ls)
elif a<=len(ls)-1 and b<len(ls)-1 and b<a:
    for i in range(b,a):
        ls.pop(i)    
    print(ls)
else:
    a>len(ls)-1 or b>len(ls)-1
    print('error')
