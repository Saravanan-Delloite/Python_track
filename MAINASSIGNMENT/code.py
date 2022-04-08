from operations.adminOp import adminOperation
from operations.userOp import userOperations
print("Select a option\n1.Admin Login\n2.User Login\n3.Exit ")
choise=int(input())
match choise:
    case 1:
        #Admin operations
        operations=adminOperation()
        while(True):
            if (operations.login()):
                print("Login successful")
                break
            else:
                print("Enter the correct password")
        operations=adminOperation()
        operations.functions()
    case 2:
        #User operations
        operation=userOperations()
        operation.userFunctions()
    case 3:
        #Exiting the program
        print("Successfully exited")
        exit()
