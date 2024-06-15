def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    for i in range(0,a):
        a=a*10**(i+1)+a
    print(a)
main()

