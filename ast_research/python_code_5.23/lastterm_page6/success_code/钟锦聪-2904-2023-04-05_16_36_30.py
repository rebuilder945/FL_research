def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    n = 0
    m = str(a)
    sum = []
    for i in range(1,a+1):
        x = m*i
        sum.append(int(x))
    for t in range(a):
         n += sum[t]
    print(n)
main()

