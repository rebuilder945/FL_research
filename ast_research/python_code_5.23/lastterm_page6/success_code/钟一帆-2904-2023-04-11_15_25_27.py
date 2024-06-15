def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
        s=0
        m=a
        n=0
        while m>0:
                s+=(n+1)*a*10**(m-1)
                m-=1
                n+=1
        print(s)
main()

