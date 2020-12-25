def fact(i):
    if i==1 or i==0:
        return i
    else:
        return i*fact(i-1)
