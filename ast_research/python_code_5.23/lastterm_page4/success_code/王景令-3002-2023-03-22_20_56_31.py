a = eval(input())
b = sum(a)/len(a)
if b == int(b):
    print(int(b))
else:
    print('%.2f'%b)

