def anagramSolution(s1,s2):
    if len(s1)!=len(s2): #长度不同，直接结束
        return False
    list_1=list(s1) #将s1存入列表中
    n=len(s1) 
    for c in s2: #枚举第一个单词的每一个字母
        found = False #先定义False，假设找不到
        for i in range(n): #在列表s1中查找c
            if list_1[i]==c:
                return True 
                list_1[i]=None #做记号，找到就打勾
                break
        if not found: 
            return False
    return True
x=eval(input())
y=eval(input())
print(anagramSolution(x,y)) 
