lista=eval(input())
sb=sum(lista)/len(lista)
if sum(lista) % len(lista) == 0:
    print("%d"%(sb))
else:
    print("%.2f"%(sb))

