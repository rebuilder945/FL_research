def main():
    a=int(input())
    calculate_sum(a)
def  calculate_sum(x):
        s=0
        for i in range(x):
              s+=(i+1)*x
        print(s)
main()

