list=eval(input())
a=sum(list)
pingjun=a/(len(list))
if int(pingjun)==pingjun:
    print("%.1d"%pingjun)
else:
    print("%.2f"%pingjun)

