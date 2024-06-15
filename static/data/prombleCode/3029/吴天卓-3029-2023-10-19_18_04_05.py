xing=input().split(",")
marks=eval(input())
A=[]
B=[]

for i in range(len(xing)):
    A.append(xing[i])
    A.append(marks[i])
    C=A.copy()
    B.append(C)
    A.clear()
print(B)
