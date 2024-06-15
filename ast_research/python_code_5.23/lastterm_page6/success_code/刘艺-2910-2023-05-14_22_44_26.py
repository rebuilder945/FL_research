h = eval(input())
N = eval(input())
ls = [h]
a = 0
while a < N-1:
    ls.append(h)
    h = h*0.5
    a += 1
sum = sum(ls)
print("%.2f"%(sum))
