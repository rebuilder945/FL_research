h = eval(input())
N = eval(input())
a = [10]
if N == 1:
    print(h)
else:
    for x in range(1,N+1):
        a.append(h*(0.5)**(x-1))
        h = h*(0.5)**x
    print(sum(a))
