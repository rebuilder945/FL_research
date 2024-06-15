a=eval(input())
numbers=[]
for i in a:
    if a.count(i)==1:
        numbers.append(i)
numbers.sort()
if numbers==[]:
    print('False')
else:
    for x in numbers:
        print(x,end=',')


