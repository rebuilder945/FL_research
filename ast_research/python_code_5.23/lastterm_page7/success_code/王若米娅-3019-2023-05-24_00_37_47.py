str1=input()
ls=str1.split(" ")
ls1=[eval(ls[1]),eval(ls[2]),eval(ls[3])]
ls1.sort(reverse=True)
sum=eval(ls[1])+eval(ls[2])+eval(ls[3])
avg=sum/3
print(ls[0],end=" ")
print("%.2f"%(ls1[0]),end=" ")
print("%.2f"%(ls1[1]),end=" ")
print("%.2f"%(ls1[2]),end=" ")
print("%.2f"%(avg),end=" ")

