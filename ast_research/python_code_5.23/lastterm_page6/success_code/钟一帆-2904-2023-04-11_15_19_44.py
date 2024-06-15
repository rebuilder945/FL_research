def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
        s=0
        m=a
       
        if m>0:
                s+=a*10**(m-1)
                m-=1
        print(s)
main()

