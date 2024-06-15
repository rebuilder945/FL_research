ls1 = eval(input())
ls2 = []
for i in range(len(ls1)):
   ls2.append(max(ls1))
if ls2[0]==0:
    print("0")   
else:
    a = "".join(str(i) for i in ls1)
    print(a)
    


