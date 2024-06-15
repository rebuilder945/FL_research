def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=""
    c=0
    for i in range(a):
        b=b+str(a)
        c=c+int(b)
    print(c)
main()

