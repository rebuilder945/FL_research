def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        s = sum(int(str(a)*i) for i in range(1,a+1))
        print(s)
main()

