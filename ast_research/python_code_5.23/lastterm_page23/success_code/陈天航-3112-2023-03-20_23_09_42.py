a,b,c,d=eval(input())
if d>=40:
    score=a+b+c+d*0.7
else:
    score=d
print("%.2f"%score)
minscore=(60-a-b-c)/0.7
print("%.2f"%minscore)


