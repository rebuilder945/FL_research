ll=eval(input())
n=ll.count(0)
for i in range(n):
    ll.remove(0)
    ll.append(0)
print(ll)
