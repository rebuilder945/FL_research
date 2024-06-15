list=eval(input())
a,b=eval(input())
if a<len(list)-1 and b<=len(list)-1 and a<=b:
    for i in range(a,b):
        list.pop(i) 
    print(list)
elif a<=len(list)-1 and b<len(list)-1 and b<a:
    for i in range(b,a):
        list.pop(i)    
    print(list)
else:
    a>len(list)-1 or b>len(list)-1
    print('error')
