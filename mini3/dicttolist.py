class Conversion:
    def DictToList(self,dict):
        lst=[]
        for j in range(len(list(dict.keys()))):
            temp = []
            temp.append(list(dict.keys())[j])
            for k in range(len(list(dict.values())[j])):
                temp.append(list(dict.values())[j][k])
            lst.append(temp)
        print(lst)
dict={"HuEx": [1, 3, 4],
      "is": [7, 6],
      "best": [4, 5]}
convert=Conversion()
convert.DictToList(dict)