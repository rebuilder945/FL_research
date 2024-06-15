def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=0
    for x in range(1,a+1):
        s=str(a)*x
        b+=int(s)
    print(b)
main()

