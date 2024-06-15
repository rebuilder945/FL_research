a=eval(input())
if sum(a)%len(a)==0:
    print(int(sum(a)/len(a)))
elif sum(a)/len(a)<1:
    print(0)
else:
    b=sum(a)/len(a)
    print('%.2f'%b)
