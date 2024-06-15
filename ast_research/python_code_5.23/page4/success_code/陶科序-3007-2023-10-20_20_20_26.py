lst = eval(input())
a,b = eval(input())
a = int(a)
b = int(b)
if a<len(lst) and b<len(lst):
    if a <b:
        del list[a:b]
        print(lst)
    else:
        del lst[b+1:a+1]
        print(lst)
else:
    print("error")
