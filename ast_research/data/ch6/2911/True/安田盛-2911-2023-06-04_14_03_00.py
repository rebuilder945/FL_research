n=input()
a=[int(x) for x in n]
for i in range(len(n)):
    a[i]=str((a[i]+5)%10)
a.reverse()
print("".join(a))






    





