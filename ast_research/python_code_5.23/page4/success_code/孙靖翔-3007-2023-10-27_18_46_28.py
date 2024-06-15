lst=[]
ss=input("").split(",")
n,m=eval(ss[0]),eval(ss[1])
def main():
    if n>len(lst) or m>len(lst):
        print("error")
        return
    elif n<m:
        lst=lst[:n]+lst[m:]
    elif n>m:
        lst=lst[:m+1]+lst[n+1:]
    print(lst)
