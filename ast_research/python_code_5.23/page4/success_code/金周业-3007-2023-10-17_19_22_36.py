list1=eval(input())
m,n=eval(input())
if m<len(list1) and n<len(list1):
    for i in range(m-n):
        del list1[n]
    print(list1)
else:
    print("error")





