list = eval(input())
a = eval(input())
if a[0] >= len(list):
    print("error")
elif a[1] >= len(list):
    print("error")
elif a[0]>=a[1]:
    print("error")
else: 
    for i in range(a[1]-a[0]):
        del list[a[0]]
    print(list)
