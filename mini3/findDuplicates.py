from collections import Counter

class Duplicate:
    def DuplicateValue(self,value):
        lst=[]
        val=[]
        for i in range(len(value)):
            res = Counter(value[i])
            for j in range(len(list(res.values()))):
                if(((list(res.values()))[j]) > 1):
                    lst.append((list(res.keys()))[j])
                    val.append((list(res.values()))[j])
        for i in range(len(lst)):
            print(lst[i],"->",val[i])

numbers=[[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
duplicate = Duplicate()
duplicate.DuplicateValue(numbers)