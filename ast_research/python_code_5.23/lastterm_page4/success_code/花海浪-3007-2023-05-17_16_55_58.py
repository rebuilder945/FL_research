lst=eval(input())
n,m,=eval(input())
if int(n)>=int(m) or int(n)>len(lst) or int(m)>len(lst):
    print("error")
else:
    for i in range(int(n),int(m)):
        del lst[i]
    print(lst)

