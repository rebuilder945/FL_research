h = eval(input())
N = eval(input())
ls = [h]
i = 1
while i < N:
    i = i+1
    ls.append(h)
    h = h*0.5
m = sum(ls)
print("%.2f"%m)
