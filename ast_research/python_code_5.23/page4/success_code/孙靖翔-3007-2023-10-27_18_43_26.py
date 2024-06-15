lst=input()[1:-1].split(",")
n,m=eval(input()).split(",")
def main():
    if n>len(lst) or m>len(lst):
        print("error")
        return
    elif n<m:
        lst=lst[:n]+lst[m:]
    elif n>m:
        lst=lst[:m+1]+lst[n+1:]
    print(lst)
