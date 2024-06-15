names=list(input().split(","))
scores=eval(input())
num=len(scores)
lst=[]
for i in range(num):
    pin=[]
    pin.append(names[i])
    pin.append(scores[i])
    lst.append(pin)
print(lst)

    
