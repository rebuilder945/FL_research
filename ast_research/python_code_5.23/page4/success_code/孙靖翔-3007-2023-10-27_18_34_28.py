lst=eval(input(""))
def main():
    lst=input()[1:-1].split(",")
    lst=[eval(i) for i in lst]
    ss=input("").split(",")
    n,m=eval(ss[0]),eval(ss[1])
    if n>len(lst) or m>len(lst):
        print("error")
        return
    elif n<m:
        lst=lst[:n]+lst[m:]
    elif n>m:
        lst=lst[:m+1]+lst[n+1:]
    print(lst)

