list_1=list(eval(input()))
a=0
for i in list_1:
    a+=i
ave=a/len(list_1)
if ave%1==0:
    print(int(ave))
else:
    print("%.2f"%(ave))

