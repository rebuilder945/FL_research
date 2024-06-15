def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=[a]
        d=str(a)
        for i in range(a-1):
                c=d*i
                b.append(int(c))
        print(sum(b))
main()

