def shuixianhua(n):
    
        if int(str(n)[0])**3+int(str(n)[1])**3+int(str(n)[2])**3==i:
            return True
        else:
            return False
n=eval(input())
a=[]
for i in range(100,n):
     if shuixianhua(n):
          print(n)
          a.append(n)
if a==[]:
     print("none")

