# n=input()        哪里错误？？
# a=eval(input())
# v=eval(input())
# l=v*v/a/2
# print("The acceleration of %s is %.2f M/s, the take-off speed is %.2f M/s, and the shortest take-off runway length is %.2f M."%(n,a,v,l))
#n=input()
#a=eval(input())
#v=eval(input())
#l=v*v/a/2
#print("The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and the shortest take-off runway length is %.2f M." % (n,a,v,l ))

#b=eval(input())     # 格式错误？？
#g=eval(input())
#pb=b/(b+g)*100
#pg=g/(b+g)*100
#print("The male students ratio is %.2f%%,the female students ratio is %.2f%%"%(pb,pg))   # 格式错误？？---the female前,无需空格，因为题目里面没有空格！

#a=eval(input())
#b=a/43560
#print("The land area is %.3f"%b)

a=eval(input().split())
b=eval(input().split())
lst1=list[a]
lst2=list[b]
s=(lst1[0]-lst2[0])**2+(lst1[1]-lst2[1])**2
l=s**0.5
print("%.2f"%l)
