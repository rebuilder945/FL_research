lst=eval(input())
n,m=eval(input())
for x in range(n,m):
        if m<len(lst):
            del lst[x]
            print(lst)
else:
    print("error")
