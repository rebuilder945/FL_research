def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=str(a)
        c=[b*i for i in range(1,a+1)]
        d=list(map(int,c))
        print(sum(d))
main()

