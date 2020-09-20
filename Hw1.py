def syracuse(n):
    print(n)
    if (n==1):
        return 1
    elif (n%2 == 1):
        return syracuse(3*n+1)
    else:
        return syracuse(n/2)
    