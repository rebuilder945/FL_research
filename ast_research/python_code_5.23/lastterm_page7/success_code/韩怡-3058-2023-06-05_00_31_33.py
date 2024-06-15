st=input() or "q"
dic={}
while st != "q":
    i=input()
    dic[i]=dic.get(i,0)+1
    st=input() or "q"
print(max(i,dic.get),max(dic.values()))

