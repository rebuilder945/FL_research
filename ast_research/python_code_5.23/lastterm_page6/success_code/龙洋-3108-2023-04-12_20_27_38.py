lis=input()
lis1=[]
for x in range(26):
    q=0
    xiang=chr(x+ord('a'))
    for y in lis:
        q=q+y.count(xiang)
    if q>0:
        print(xiang+","+"%.d"%q)

