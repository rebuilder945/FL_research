def fenzi(i):
    list1 = [2,3]
    a= list1[0]
    b = list1[1]
    end = 1
    for x in range(i):
        if x ==0:
            end =  2
        elif x == 1:
            end =  3
        else:
            end = a+b
            a = b 
            b = end
    return end
def fenmu(i):
    list2  = [1,2]
    a = list2[0]
    b = list2[1]
    end = 1
    for x in range(i):
        if x == 0:
            end =1
        elif x == 1:
            end = 2
        else:
            end = a+b
            a = b
            b = end
    return end
m = eval(input())
k = 0
for y in range(1,m+1):
    j = fenzi(y)/fenmu(y)
    k+=j
print("%.4f"%(k))

