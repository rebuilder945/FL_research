def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    c=[]
    for i in range(0,a):
        b=a*(a-i)*10**i
        c.append(b)
    s=sum(c)
    print(s)
main()

