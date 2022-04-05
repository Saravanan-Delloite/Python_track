class Dictionary:
    def MapDictionary(self,keys,values):
        dict={}
        for i in range(len(keys)):
            dict[keys[i]] = values[i]
        print(dict)

Keys = ["Ten", "Twenty", "Thirty"]
Values = [10, 20, 30]
dictionary = Dictionary()
dictionary.MapDictionary(Keys,Values)