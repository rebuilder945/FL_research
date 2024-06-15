A=eval(input())
A.sort(reverse=True)
B=[str(i) for i in A]
print(''.join(B))
if A == [0,0,0]:
    print(0)
