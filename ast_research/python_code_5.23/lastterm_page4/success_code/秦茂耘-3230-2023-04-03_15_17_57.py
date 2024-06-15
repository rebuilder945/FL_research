A=eval(input())
A.sort(reverse=True)
if A == [0,0,0]:
    print(0)
else:
    B=[str(i) for i in A]
    print(''.join(B))

