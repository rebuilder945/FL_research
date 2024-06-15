def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m=0
    e=0
    for x in range(num+1):
        A=[x for x in range(x)]
        m=m+1/sum(A)
        e+=m
    print(e)
main()


