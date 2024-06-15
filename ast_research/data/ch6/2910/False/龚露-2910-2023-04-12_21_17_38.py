from re import S


h = eval(input())
N = eval(input())
i = 1
s = 0
while i < N + 1:
    s = s + h*0.5
    h = h*0.5
    i = i+1
print("%.2f"%s)
