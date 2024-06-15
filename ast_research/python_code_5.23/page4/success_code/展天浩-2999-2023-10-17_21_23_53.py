lst=input()[1:-1].split()
m,n=int(input()).split()
if m>n:
    lst=lst[:n]+lst[m]+lst[n,m]+lst[n]+lst[m:]
elif n>m:
    lst=lst[:m]+lst[n]+lst[m,n]+lst[m]+lst[n:]

