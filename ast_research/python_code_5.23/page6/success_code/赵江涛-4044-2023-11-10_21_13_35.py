from re import I


n = eval(input())
f = 0
for i in range(2,n+1):
     g = i % 10
     s = i //10%10
     b = i //100%10
     if g**3+s**3+b**3 == i:
        print(i)
        f+=1
if f == 0:
    print('none')
