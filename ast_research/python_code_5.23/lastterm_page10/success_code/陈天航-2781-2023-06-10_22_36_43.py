a=input()
b=input()
list_a=[]
for i in a:
    list_a.append(i)
list_b=[]
for t in b:
    list_b.append(t)
list_a.sort()
list_b.sort()
if list_a==list_b:
    print("True")
else:
    print("False")

