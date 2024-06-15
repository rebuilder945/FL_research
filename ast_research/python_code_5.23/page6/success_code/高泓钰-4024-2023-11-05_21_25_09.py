def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    lst=[]
    n=0
    m=a
    s=0
    while n<a:
        s=s+m*10**n
        n=n+1
        lst.append(s)
    y=0
    for x in lst:
        y=y+x
    print(y)

main()

