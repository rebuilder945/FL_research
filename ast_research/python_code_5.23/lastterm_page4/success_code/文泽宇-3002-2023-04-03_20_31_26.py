lst = eval(input())
pingjun = sum(lst)/len(lst)
if pingjun == int(pingjun):
    print(pingjun)
else:
    print("{:.2f}".format(pingjun))
