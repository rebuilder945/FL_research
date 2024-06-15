def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    s=0
    m=0
    n=0
    while n < a:
        m += m*10+a
        s=m+s
        n+=1
    print(s)
main()

