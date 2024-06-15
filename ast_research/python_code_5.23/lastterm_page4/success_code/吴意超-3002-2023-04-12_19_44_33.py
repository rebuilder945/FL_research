a = eval(input())
eva = sum(a)/len(a)
if(eva%1 == 0):
    print(int(eva))
else:
    print("%.2f"%(eva))

