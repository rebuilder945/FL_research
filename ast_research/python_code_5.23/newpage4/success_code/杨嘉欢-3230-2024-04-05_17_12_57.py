input = input()
if (len(input) > 2): 
    input = input[1:-1]
    inputArray = input.split(",")

    inputArray.sort(reverse=True)
    result=0
    for i in inputArray:
        if result != 0:
            result *= 10
        result+=int(i)
print(result)

# for b in a:
#     numbers=[]
#     if b == int():
#         b = int(b)
#     else:
#         continue
#     numbers.append(b)
    
# numbers.sort(reverse=True)
# result=""
# for i in numbers:
#     result+=str(i)
# result=eval(result)
# print(result)

