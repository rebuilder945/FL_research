def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b = []
    for i in range(1,a+1):
        si = (a*(a+1-i))*(10**(i-1))
        b.append(si)
        p = sum(b)
    print(p)
main()

