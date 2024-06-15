def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(l):
    sum=0
    for x in range(1,l+1):
        c=lll(x,l)
        sum+=c
    print(sum)
def lll(p,m):
    m=str(m)
    s=m*p   
    s=int(s)
    return s
main()

