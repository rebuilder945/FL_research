lista=eval(input())
n=sum(lista)/len(lista)
if sum(lista) % len(lista) == 0:
    print("%d"%n)
else:
    print("%.2f"%n)


