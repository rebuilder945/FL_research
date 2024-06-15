def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    total=0
    for i in range(1,a+1):
        total+=a*10**(i-1)
    print(total)
main()

