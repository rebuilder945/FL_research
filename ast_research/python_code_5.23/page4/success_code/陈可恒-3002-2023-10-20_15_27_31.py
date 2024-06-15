a = eval(input())
b = sum(a)/len(a)
s = str(b).split('.')
if float(s[1])==0:
    print(int(b))
else:
    print('%.2f'%b)
