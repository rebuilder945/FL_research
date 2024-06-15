numbers=eval(input())
a=1
rnewlist=[]
for i in numbers:
 if numbers.count(i) == a:
    rnewlist.append(i)
rnewlist.sort()
rnewlist=",".join(str(i) for i in rnewlist)
if rnewlist:
   print(rnewlist)
else:
   print("False")
