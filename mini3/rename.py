class Update:
    def RenameInDictionary(self,dict):
        dict["Location"] = dictpop("city")
        print(dict)

dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"
}
update=Update()
update.RenameInDictionary(dict)