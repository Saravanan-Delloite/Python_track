class MergeList:
    def ListMerge(self,lst1,lst2):
        merge_list=[]
        for i in range(len(lst1)):
            for j in range(len(lst2)):
                merge_list.append(lst1[i]+lst2[j])
        print(merge_list)


lst1 = ["Hello ", "take "]
lst2 = ["Dear", "Sir"]
merge=MergeList()
merge.ListMerge(lst1,lst2)