a=float(input())
b=int(input())
h=[a*0.5**i for i in range(b)]
total=h[0]+sum(h[1:])*2
print('%.2f' %total)
