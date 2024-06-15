def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m=0
    e=0
    for x in range(num+1):
        A=[i for i in range(x+1)]
        if len(A)==0:
            m=0
        else:
            m=m+1/sum(A)
        e+=m
    print(e)
main()


