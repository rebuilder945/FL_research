def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    for i in range(1,a+1):
        s = 0
        s += a*(10**(a-1))
     return s
    print(s)

main()

