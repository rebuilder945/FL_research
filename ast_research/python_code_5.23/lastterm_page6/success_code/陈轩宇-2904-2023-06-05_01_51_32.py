def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    c=a
    sum1 = 0
    n=1
    save = []
    save.append(sum1)
    while n<a*10**(a-1):
        sum1+=c*n
        n = n*10
        save.append(sum1)
    b = sum(save)
    print(b)
main()

