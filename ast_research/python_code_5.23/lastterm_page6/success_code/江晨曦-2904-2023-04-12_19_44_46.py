def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    y = []
    for i in range(x):
        m = str(x)
        z=eval(m*i)
        y.append(z)
    print(sum(y))     
main()

