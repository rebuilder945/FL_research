lst=eval(input())
num=""
for i in lst:
    a=lst.count(i)
    if a==1:
        num+=(str(i))
        #print("False")     
lstnum=list(str(num))
lstnum.sort()
for i in lstnum:
    print(i,end=",") 
if bool(lstnum)==False:
    print("False")




