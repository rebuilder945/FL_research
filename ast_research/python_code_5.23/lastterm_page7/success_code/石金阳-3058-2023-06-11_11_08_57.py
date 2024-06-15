x={}
s=input()
while s!="q":
    x[s]=x.get(s,0)+1
    s=input() #这里加s=input()作用是什么
    #题目的要求是输入不定行，也就是说我们不知道要输入多少行，在不满足结束条件的情况下持续输入即可，所以这里的输入是放在循环里面的，只要满足条件就一直继续输入
print(max(x,key=x.get),end=" ")
print(max(x.values()))


