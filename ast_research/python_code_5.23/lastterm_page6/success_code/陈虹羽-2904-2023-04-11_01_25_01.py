def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
        b=0
        for i in range(a):
                b=b+(i+1)*a*10**(a-i-1)
        print(b)
main()

