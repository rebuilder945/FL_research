def main():
    a = input()
    print(strreduce(a))

def strreduce(a):
    b=""
    for i in a:
         if i not in b:
             b+=i
    return b


main()


