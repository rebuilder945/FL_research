lst=eval(input())
save=[]
for i in lst:
    if i not in save:
        save.append(i)

print(save[::-1])
# # 这个又是哪里不对啊啊啊啊！！！！！

# lst=eval(input())
# save=[]
# for i in range(len(lst)-1,-1,-1):         # 对的在这里    看不懂哇看不懂哇
#     if lst[i] not in save:
#         save.append(lst[i])
# save.reverse()
# print(save)
