class NestedList:
    def Nested(self,lst1,lst2):
        for i in range(len(lst2)):
            lst1[2][1][2].append(lst2[i])
        print(lst1)

lst1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
lst2=["h", "i", "j"]
nest=NestedList()
nest.Nested(lst1,lst2)