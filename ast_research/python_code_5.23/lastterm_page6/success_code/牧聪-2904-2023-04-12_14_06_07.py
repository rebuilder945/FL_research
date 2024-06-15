def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    m=0
    num=[]
    for x in range(1,a+1):
        m=a*10**(x-1)+m
        num.append(m)
    print(sum(num))
main()

