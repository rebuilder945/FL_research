h = eval(input())
N = eval(input())
a = [h]
if N == 1:
    print(h)
else:
    for x in range(1,N):
        a.append(h)
        h = h/2
    print('%.2f'%sum(a))
