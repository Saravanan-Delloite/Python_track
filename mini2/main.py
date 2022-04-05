n=3
for i in range(1,n+1):

    x=1
    for j in range(1,i+1):
        print(' ',x,sep='',end='')
        x=x*(i-j)//j
    for j in range(0,n-i):
        print(' ',0,sep='',end='')
    print()



