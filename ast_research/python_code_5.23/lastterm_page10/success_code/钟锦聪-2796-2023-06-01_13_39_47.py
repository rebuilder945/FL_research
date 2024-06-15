ls = input()
num =[]
for x in ls:
    if not "0"<=x<="9":
        num.append(" ")
    else:
        num.append(x)
str = "".join(num)
ilist = []
nem  =str.split()
if nem==[]:
    print("No digits")
else:
    for x in nem:
        c = len(x)
        ilist.append(c)
    for x in nem[-1::]:
        if x!='':
            if len(x)==max(ilist):
                print(int(x))
                break
  


