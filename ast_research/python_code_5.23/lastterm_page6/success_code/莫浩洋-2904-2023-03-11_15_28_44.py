def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(x):
        s=0
        s1=0
        for i in range(x):
              s+=10**i*x
              s1+=s
        print(s)
main()

