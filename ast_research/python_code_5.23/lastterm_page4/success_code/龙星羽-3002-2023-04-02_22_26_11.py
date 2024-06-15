num=eval(input())
n=sum(num)/len(num)
if n==int(n):
    print(int(n))
else:
    print('%.2f'%n)
