def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s=[]
    for i in range(0,num+1):
        w=1/j(i)
        s.append(w)
    e=sum(s)
    print('%.6f'%e)
    # e=1+1/1!+1/2!+1/3!+…+1/num!
def j(num):
    a=1
    for i in range(1,num+1):
        a*=i
    return a
main()


