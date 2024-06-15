def shuixianhuashu(a):
    if a>=100:
        for i in range(100,a+2):
            if i==int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3:
                print(i)
            
    else:
        print("none")
a=eval(input())
shuixianhuashu(a)
# 
# n=input()
# flag=False
# for i in range(100,min(eval(n)+1,1000)):
#     if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3==i:
#         print(i)
#         flag=True
# if flag==False:
#     print("none")
