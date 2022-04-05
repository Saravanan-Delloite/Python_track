for i in range(1,5):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("\n")
for i in range(5,0,-1):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print("\n")
#second pattern
for r in range(1,5):
    for c in range(1,8):
        if r==4 or r+c==5 or c-r==3:
            print("*",end="")
        else:
            print(end=" ")
    print()
#third pattern
for i in range(0,5):
    for j in range(0,i+1):
        print(" "*2,end=" ")
    for j in range(i,5):
        if(j==i or j==4 or i==0):
            print(" * ",end="")
        else:
            print("  ",end=" ")
    print()

