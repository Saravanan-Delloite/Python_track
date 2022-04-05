from itertools import combinations
class StringClass:
    def __init__(self):
        self.st="12314532"
    def length(self):
        return len(self.st)
    def splitst(self):
        arr= [i for i in self.st]
        return arr
class1=StringClass()
class1.length()
split=class1.splitst()

class PairsPossible(StringClass):
    def possiblePairs(self):
        res=[]
        res =list(combinations(self.st, 2))
        return res
    def printPairs(self,elm):
        self.elm=elm
        print("{} ".format([i for i in self.elm]))
lst=[]
class2=PairsPossible()
lst=class2.possiblePairs()
class2.printPairs(lst)
class SearchCommonElements(StringClass):
    commonlst=[]
    def checkString(self,st):
        self.st=st
        for i in self.st:
            if self.st.count(i)<1:
                self.commonlst.append(i)
        return self.commonlst
class3=SearchCommonElements
lst2=class3.checkString(split)
