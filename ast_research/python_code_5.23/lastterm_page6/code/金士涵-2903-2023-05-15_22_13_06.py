def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    n=1
    e=1
    for i in range(1,num+1):
        n = n*i
        e = e+1/n
if e=2:
    print("2.000000")
else:
    print(round(e,6))

main()


