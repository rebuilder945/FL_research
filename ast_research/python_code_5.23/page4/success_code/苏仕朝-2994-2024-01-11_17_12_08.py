list=list(eval(input()))
n,m=eval(input())
len=len(list)
if n <(-len) or n>=len-1:
    print("error")
elif n>=(-len) and n<len-1:
    a=list[n]
    while m>0:
        list.append(a)
        m-=1
    print(list)
