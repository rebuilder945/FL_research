m=eval(input())
w=eval(input())
m1=m/(m+w)*100
w1=w/(m+w)*100
m2=round(m1,2)
w2=round(w1,2)
m=str(m2)+'%'
w=str(w2)+'%'
print("The male students ratio is %s,the female students ratio is %s"%(m,w))
