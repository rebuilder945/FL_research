def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n=0
    m=a
    s=0
    while n<a:
        s=m*a*10**n+s
        n+=1
        m-=1
       
    print(s)

main()

