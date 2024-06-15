list1 = list(eval(input()))
n,m = eval(input())
list2 = list1.copy()
if n>=len(list1) and m<len(list2):
    for x in range (n,m):
        list2.remove(list1[x])
    print(list2)

else:
    print("error")

