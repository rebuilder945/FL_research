h = eval(input())
N = eval(input())
a = [h]
if N == 1:
    print(h)
else:
    for x in range(1,N+2):
        a.append(h*(0.5)**(x-1))
        h = h*(0.5)**x
    print('%.2f'%sum(a))
