a = input()
lst=[]
while a != '#':
    lst.append(int(a))
    b = input()
    a = b
print(len(lst),sum(lst))
    
