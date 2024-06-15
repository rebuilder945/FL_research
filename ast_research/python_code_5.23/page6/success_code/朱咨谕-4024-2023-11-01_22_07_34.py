def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=a
    tot=0
    for i in range(a):
        tot+=b
        b=b*10+a
    print(tot)
main()

