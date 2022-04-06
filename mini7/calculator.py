from aifc import Error
class FormulaError(Error):
    pass
def checkLen(lst):
    if len(lst)!=3:
        raise FormulaError("you must include 3 elements which includes operator and two numbers")
def checkType(lst):
    try:
        lst[0] = float(lst[0])
        lst[2] = float(lst[2])
    except:
        raise FormulaError("you have to give two numbers to perform the operation")

    if lst[1] == "+" or lst[1] == "-":
        pass
    else:
        raise FormulaError("you have to enter a correct operator to perform the action")
    return lst
def perform(lst):
    if lst[1]=="+":
        print(lst[0]+lst[2])
    else:
        print(lst[0]-lst[2])
print("enter a action :",end="")
string = input()
flag=False
while(string):
    if flag:
        print("enter a action or type quit :",end="")
        string = input()
        if string=="quit":
            exit()
    string = string.split(" ")
    checkLen(string)
    lst = checkType(string)
    perform(lst)
    flag=True