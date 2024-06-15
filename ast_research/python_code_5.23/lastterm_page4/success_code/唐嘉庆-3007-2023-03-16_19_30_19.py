lst=eval(input())
b,c=eval(input())
jack=[]
if b >len(lst) or c> len(lst):
    print('error')
    
else:
    for i in range(b,c):
        jack.append(lst[i])
    for x in jack:
       if x in lst:
        lst.remove(x)
    print(lst)
