A = eval(input())
A.reverse()
B = [""]
for i in A:
    if i not in B:
        B.insert(0,i)
B.pop()
print(B)
