def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(a):
        s=0
        n=str(a)
        for i in range(1,a+1):
                s+=int(n*i)
        print(s)
main()

