def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 1                     #  e = 1
    m = 1                     #  for x in range(num):
    n = 0  #计算阶乘的技巧     #  m = 1
    while n < num :           #  for y in range(x+1):
        m *= n + 1            #     m *= y+1
        n += 1                #  e += 1/m
        e += 1/m
    print("%.6f"%e)
main()


