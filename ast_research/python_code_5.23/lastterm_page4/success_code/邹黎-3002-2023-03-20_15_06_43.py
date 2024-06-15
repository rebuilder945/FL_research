list=eval(input())
total=0
for x in list:
    total+=x
pingjun=total/(len(list))
if type(pingjun)==int:
    print("%.1d"%pingjun)
elif type(pingjun)==float:
    print("%.2f"%pingjun)

