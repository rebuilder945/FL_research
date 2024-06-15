def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=[a]
        d=float(a)
        for i in range(a):
                d+=d
                b.append(int(d))
        print(sum(b))
main()

