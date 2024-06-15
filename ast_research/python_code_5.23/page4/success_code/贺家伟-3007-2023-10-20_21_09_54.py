lst=input()
lst=[eval(i) for i in lst]
ss=input("").split(",")
n,m=eval(ss[0]),eval(ss[1])
if n>len(lst) or m>len(lst):
        print("error")
elif n<m:
        lst=lst[:n]+lst[m:]
        print(lst)
elif n>m:
        lst=lst[:m+1]+lst[n+1:]
        print(lst)
