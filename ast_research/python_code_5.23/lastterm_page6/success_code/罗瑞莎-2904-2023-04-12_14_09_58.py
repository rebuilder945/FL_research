def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    for i in range(1,a+1):
        a=a*10+a
    print(a)
main()

