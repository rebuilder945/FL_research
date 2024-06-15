ls1 = eval(input())
ls2 = []
for i in range(len(ls1)):
   ls2.append(max(ls1))
   ls1.remove(max(ls1))
if ls2[0]==0:
    print("0")   
else:
    a = "".join(str(i) for i in ls2)
    print(a)
    


