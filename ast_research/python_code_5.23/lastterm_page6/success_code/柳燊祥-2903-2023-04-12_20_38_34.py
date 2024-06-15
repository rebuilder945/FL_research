def main():
    num = eval(input())
    calculate_e(num)
def p(i):
    if i==0:
        return 1
    else:
        return i*p(i-1)
def calculate_e(num):
    e=[]
    i=0
    while i<num:
        x=1/p(i)
        e.append(x)
        i=i+1
    print(sum(e))

main()


