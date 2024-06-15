a=input()
b=input()
words=a.split()
lst_a=list(words)
for i in lst_a:
    if b in lst_a:
        lst_a.remove(b)
for x in lst_a:
    print(x,end=" ")
