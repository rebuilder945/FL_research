x={}      #创建一个字典
s=input()    #字符串的输入
while s!='q':       #因为程序最后用‘q’来判断结束，所以使用while循环
    x[s]=x.get(s,0)+1     #get()新建字典(键：值)并存入字典x
    s=input()       #继续输入字符串
print(max(x,key=x.get),end=" ")      #将返回一个字典x的值最大的项。即对应于最大值的键。
print(max(x.values()))    #输出对应的值
