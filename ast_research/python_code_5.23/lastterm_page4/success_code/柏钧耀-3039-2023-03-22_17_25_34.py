a=eval(input())
if a ==[]:
    print([])
else:
     maxi=a[max(a)].count()
     minn=a[min(a)].count() 
     for i in range(maxi):
          a.remove(max(a))
     for i in range(minn):
          a.remove(min(a))
print(a)
