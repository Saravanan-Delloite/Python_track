class MergerDictionaries:
    def Merger(self,dict1,dict2):
        dict1.update(dict2)
        print(dict1)


lst1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
lst2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
merge=MergerDictionaries()
merge.Merger(lst1,lst2)