a = eval(input())
new = []
count = 0
count2 = 0
for x in a:                    # 33399
    for i in a:
        if x == i:
            count +=1
    if count>1:
        count2+=1
if count2 == len(a):
    print("False")
else:
    for x in a :
        if a.count(x) ==1:
            new.append(x)
    new.sort()
    print(*new,sep=',')
    



