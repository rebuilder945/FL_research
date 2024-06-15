count=0
total_sum=0
while True:
    user_input=input().strip()
    if user_input=="#":
        break
    number=int(user_input)
    count+=1
    total_sum+=number
print(f"{count} {total_sum}")
