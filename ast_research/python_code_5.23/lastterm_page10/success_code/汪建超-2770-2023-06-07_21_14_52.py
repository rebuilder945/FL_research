a = input()
b = input()
if len(a)!=len(b):
    print("False")
# elif a==b:
#     print('False')
else:
    lst = [i for i in a]
    lst2 = [i for i in b]
    for i in range(len(lst)):
        s=lst[i]
        if b.find(s) != -1:
            del lst2[0]
    if len(lst2)==0:
        print('True')
    else:
        print('False')
