mylist=(eval(input()))
n,m=eval(input())
if n>0 and n >=len(mylist):
    print("error")
elif n<0 and abs(n)>len(mylist):
    print("error")
else:
    temp=[mylist[n]]*m
    mylist=mylist+temp
    print(mylist)


