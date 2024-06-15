li=eval(input())
li.sort()
li.reverse()
sum=""
for i in range(len(li)):
    sum+=str(li[i])
    print(int(sum))
