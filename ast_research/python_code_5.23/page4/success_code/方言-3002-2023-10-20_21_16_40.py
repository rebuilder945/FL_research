from statistics import mean


m=eval(input())
pjs=mean(m)
if pjs==int(pjs):
    print(str(pjs))
else:
    print("%.2f"%(pjs))
