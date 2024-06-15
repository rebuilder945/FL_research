# 【问题描述】输入一个整数，输出小于等于该整数的所有水仙花数，每行输出一个，若没有水仙花数则输出“none”

# “3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身。例如：ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC。 

# 【输入形式】

        
# 【输出形式】

        
# 【样例输入】

#      100
# 【样例输出】

# none
# 【样例说明】


# 【评分标准】

#    找出所有的水仙花数则正确

n=int(input())
t=str(n)
ls=[]
for i in range (100,n+1):
    s=0
    for j in str(i):        #if int(str(i)[0])**3+int(str(i)[1])**3+int(str(i)[2])**3==i:
        s+=int(j)**3        #    print(i)
    if s==i:
        print(i)
        ls.append(i)
if len(ls)==0:
    print("none")
