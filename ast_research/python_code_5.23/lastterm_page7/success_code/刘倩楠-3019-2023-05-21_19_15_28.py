m=input().split(" ")
d=dict(name,english,python,math)(m)
avg=sum(m[1:])/3
d["avg"]=avg
d.sort()
print(d.values())
