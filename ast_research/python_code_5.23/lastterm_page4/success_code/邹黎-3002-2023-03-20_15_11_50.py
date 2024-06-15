list=eval(input())
total=0
for x in list:
    total+=x
pingjun=total/(len(list))
if int(total)==total:
    print("%.1d"%pingjun)
else:
    print("%.2f"%pingjun)

