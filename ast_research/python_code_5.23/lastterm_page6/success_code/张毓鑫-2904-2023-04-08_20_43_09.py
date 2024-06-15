def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[a]
    d=str(a)
    for i in range(a-1):
        d+=d
        b.append(int(d))
    print(sum(b))
main()

