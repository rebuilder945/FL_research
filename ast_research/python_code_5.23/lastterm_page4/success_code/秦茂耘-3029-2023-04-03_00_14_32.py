a,b,c=input().split(',')
A=[a,b,c]
B=eval(input())
C=[[x+y] for x in ''.join(A) for y in ''.join(B)]
print(C)
