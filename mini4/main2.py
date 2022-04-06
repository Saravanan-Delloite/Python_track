def count(l):
    c=l.count('A')
    d=l.count('a')
    return [c,d]

##using map function
lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
##using map function for this
listi=list(map(count,lst1))
print(listi)
##using lambda function to count total no. of 'A' and 'a'
listi2=list(map(lambda s:(s.count('A'),s.count('a')),lst1))
print(listi2)