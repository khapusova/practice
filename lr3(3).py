ch=float(input('enter human`s year(s):'))
if ch>=0 and ch<=2:
    print('in dog`s years it is:', ch*10.5)
elif ch>2 :
    sob=(ch-2)*4 + 2*10.5
    print('in dog`s years it is:', sob)
else:
    print('Error!You wrote a wrong number.')
