lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
result = filter(lambda a: a>0,map(lambda x : x*(-1),lst1))
print(list(result))