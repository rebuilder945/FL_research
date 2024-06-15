lst=input()
n,m=eval(input())
if n>len(lst) or m>len(lst):
    print("error")
else:
    lst.pop(n,m)
print(lst)

