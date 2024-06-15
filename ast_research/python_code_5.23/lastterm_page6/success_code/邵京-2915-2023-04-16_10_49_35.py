n=eval(input())
b=0
numbers=[]
for i in range(10,n+1):
    x=len(str(i))
    for a in range(x):
        c=int(str(i)[a])
        b+=c**3
    if b==i:
        numbers.append(i)
    b=0
if len(numbers)!=0:
    for i in numbers:
        print(numbers,end='')
else:
    print('none')



