n=eval(input())
sbcnm="".join(n)
cao=[(zimu,sbcnm.count(zimu)) for zimu in sorted(set(sbcnm))]
for sb,cnm in cao:
    print("{},{}".format(sb,cnm))
