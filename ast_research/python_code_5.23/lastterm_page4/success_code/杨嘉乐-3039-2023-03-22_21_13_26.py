ll=eval(input())
mx=max(ll)
mn=min(ll)
for i in range(2*len(ll)):
    if mx in ll:
        ll.remove(mx)
    if mn in ll:
        ll.remove(mn)
print(ll)
