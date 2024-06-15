lst = eval(input())
s = sum(lst)
aveg1 = s/len(lst)
aveg2 = s//len(lst)
if aveg1-aveg2==0:
    print(int(aveg1))
else:
    print("%.2f"%(aveg1))
