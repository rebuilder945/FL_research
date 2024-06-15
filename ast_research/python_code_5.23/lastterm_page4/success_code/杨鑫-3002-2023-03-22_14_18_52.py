L = eval(input())
A = sum(L)
B = A/len(L)
if B%1==0:
    print('%.0f'%B)
else:
    print('%.2f'%B)
