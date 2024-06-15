# 字符统计
                    # 输出数字之间用空格隔开
n=str(input())
e=0
k=0
s=0
l=0
for x in n:
    if x in ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']:
        e=e+1
    if x in str([i for i in range(0,10)]):
        s=s+1
    if x==' ':
        k=k+1
    else:
        l=l+1
print(e,k,s,l)   


