def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    e=[1]
    k=1
    
    while x >=0:
        for i in range(x):
            k*=x+1
            x=x-1
            k=1/k
            e.append(k)
    print(sum(e))
main()


