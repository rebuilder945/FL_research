# 字符统计
                    # 输出数字之间用空格隔开
n=str(input())
en=[]
kg=[]
shu=[]
el=[]
for x in n:
    if x in ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']:
        en.append(n.count(x))
    if x==' ':
        kg.append(n.count(x))
    if x in str([i for i in range(0,10)]):
        shu.append(n.count(x))
    else:
        el.append(n.count(x))
enz=sum(en)
kgz=sum(kg)
shuz=sum(shu)
elz=sum(el)
m=['enz','kgz','shuz','elz']
print(" ".join(m))        


