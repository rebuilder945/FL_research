a= eval(input())
b,c = eval(input())
if b<len(a):
    if c>=len(a):
        print("error")
    else:
        m = a[0:b]
        n=a[c: ]
        h = m+n
    print(h)

   
else:
    print("error")




