def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    res = 0
    s = str(a)
    for i in range(1,a+1):
        res += int(s*i)
    print(res)
main()

