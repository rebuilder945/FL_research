lst=eval(input())
lst=list(lst)
lst1=[chr(i) for i in range(ord('A'), ord('Z')+1)]
lst2=[chr(i) for i in range(ord('a'), ord('z')+1)]
for i in lst:
    if i.islower():
        for i in lst2:
            i=26-i+1
    if i.isupper():
        for i in lst1:
            i=26-i+1
print(lst)
