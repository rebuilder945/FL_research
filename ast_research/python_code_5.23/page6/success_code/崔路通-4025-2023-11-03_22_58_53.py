def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=2
    for x in range (1,num+1):
        a=[i for i in range(1,x+1)]
        if len(a)>1:
            b=[str(y) for y in a]
            c="*".join(b)
            e=e+(1/eval(c))
        
    print(e)
main()


