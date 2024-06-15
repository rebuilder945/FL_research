a=eval(input())
ll=[x+1 for x in range(a)]
ll.append(ll[0])
ll.pop(0)
print(ll)
