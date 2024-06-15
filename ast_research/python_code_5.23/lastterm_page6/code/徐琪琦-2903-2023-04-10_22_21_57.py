def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s = 1
    a = 1
    for x in range(num):
        for i in range(num):
            a = a * (i+1)                           #不可以s += 1/(i+1)!
        s = s + 1/a 
    print(%.6f"%s)
main()


