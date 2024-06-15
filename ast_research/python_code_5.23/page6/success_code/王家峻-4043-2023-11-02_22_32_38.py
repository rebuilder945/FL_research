# a=eval(input())
# b=eval(input())
# if a>=99 and b>=99:
#     print("You won a scholarship of 500 yuan!")
# elif a<=29 and b<=29:
#     print("You need to relearn!")
lst1=input()
lst2=['a','b','c','d','e','f','j','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x1 in lst2:
    jishu=0
    for x2 in lst1:
        if x2==x1:
            jishu+=1
    if jishu!=0:
        print("%c,%d"%(x1,jishu))
