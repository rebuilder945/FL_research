def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
                s=0
                t=str(a)
                for i in range(1,a+1):
                        m=t*i
                        n=int(m)
                        s+=n
main()

