n=5
for rows in range(1,n+1):
    for coloums in range(1,n+1):
        if rows == 1 or rows==n or coloums==1 or coloums==5:
            print("*",end= " ")
        else:
            print(" ",end= " ")
    print()