def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m=0
    e=0
    t=1
    for x in range(num+1):
        for i in range(x+1):
            t=t*i
            e=m+1/t
        e+=m
    print(e)
main()


