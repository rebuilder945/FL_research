a=eval(input())
a.sort()
a.reverse()
if a[0]==0:
    print("0")
else:
    b=''.join(str(i) for i in a)
    print(b)

            


        
