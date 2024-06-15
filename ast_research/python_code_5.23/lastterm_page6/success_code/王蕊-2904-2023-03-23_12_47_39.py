def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
    s=0
    n=0
    m=a
    while n<a:
        s=s+m * a * 10 **a
        n+=1
        m-=1
    print(s)
main()

