def series316(i=1, nm1=1, nm2=3):
    if (i > 2): 
        print(nm1)    
        return series316(i+1, nm2+(3*nm1), nm1)
    elif (i==1):
        return series316(i+1, 3)
    elif (i==2):
        print(nm1)
        return series316(3)
    
series316()