h=eval(input())
N=eval(input())
lst=[h]
for i in range(N-1):
    x=lst[-1]*0.5**i
    lst.append(x*2)
print(sum(lst))
