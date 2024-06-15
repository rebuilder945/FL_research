def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(a):
    b=str(a)
    c=[]
    for i in range(1,a+1):
        c.append(int(b*i))
    print(sum(c))

main()

