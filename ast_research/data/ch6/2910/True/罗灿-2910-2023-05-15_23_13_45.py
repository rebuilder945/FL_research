high=eval(input())
times=eval(input())
total=[]
for i in range(times):
    high2=high*(0.5**i)
    total.append(high2)
print("%.2f"%(sum(total)*2-high))
