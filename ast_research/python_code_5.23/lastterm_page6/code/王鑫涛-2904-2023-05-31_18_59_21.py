def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=[]
    for i in range(a):
        c=str(a)*i
        b.append(eval(c))
    print sum(b)
main()

