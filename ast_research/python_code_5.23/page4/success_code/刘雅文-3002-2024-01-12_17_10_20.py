a=eval(input())
s=sum(a)
if s%len(a)==0:
    print(int(s/len(a)))
else:
    print('%.2f'%(s/len(a)))
