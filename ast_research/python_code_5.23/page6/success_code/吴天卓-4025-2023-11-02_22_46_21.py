def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    a=1
    for i in range(x):
        c=jiecheng(i+1)
        a+=(1/c)
    print(a)
def jiecheng(q):
    b=1
    for m in range(q):
        b*=(m+1)
    return(b)
main()


