def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        s=0
        temp = a
        for i in range(1,a+1):
                s += temp
                temp = temp * 10 + a
        print(s)
main()

