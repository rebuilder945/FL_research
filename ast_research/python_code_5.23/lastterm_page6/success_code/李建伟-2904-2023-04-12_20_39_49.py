def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(n):
    lst = []
    for i in range(1,n+1):
        n = str(n)
        lst.append(int(n*i))
    sums = sum(lst)
    print(sums)
main()

