from factorial.factorial import fact
from logarithm.logarithm import *
from exp_root.root import *
from exp_root.exponentiation import *
vybor = input('Which module do you want to use?(1-factorial\ 2-exp_root\smth else-logarithm)')
if vybor=='1':
    while True:
        n = input('Enter n for factorial calculation: ')
        try:
            n = int(n)
            if n < 0:
                raise Exception
            print('factorial:'+str(fact(n)))
            break
        except Exception:
            print('Uncorrect data!')
        break
elif vybor=='2':
    while True:
        n = input('Which module do you want to use?(1-root\ 2-exponentation) ')
        try:
            if n!='1' and n!='2':
                raise Exception
            if n == '1':
                while True:
                    n1 = input('Enter n for root calculation: ')
                    try:
                        n1 = int(n1)
                        if n1 < 0:
                            raise Exception
                        print('root2:' + str(root2(n1)))
                        print('root3:' + str(root3(n1)))
                        break
                    except Exception:
                        print('Uncorrect data!')

            elif n == '2':
                while True:
                    n1 = input('Enter n for exponentation calculation: ')
                    try:
                        n1 = int(n1)
                        print('excp2:' + str(exp2(n1)))
                        print('exp33:' + str(exp3(n1)))
                        break
                    except Exception:
                        print('Uncorrect data!')
            else:
                raise Exception

        except Exception:
            print('Uncorrect data!')
        break
else:
    while True:
        n = input('Which module do you want to use?(1-log()\ 2-ln()\ 3-lg()) ')
        try:
            if n!='1' and n!='2' and n!='3':
                raise Exception
            if n == '2':
                while True:
                    b = input('Enter b calculation of e-logarithm : ')


                    try:

                        b = float(b)
                        if b < 0 :
                            raise Exception
                        print('ln=' + str(log(b)))
                        break
                    except Exception:
                        print('Uncorrect data!')
            elif n == '1':
                while True:
                    b = input('Enter b calculation of logarithm with base a: ')

                    a = input('Enter base a:')
                    try:
                        a=float(a)
                        b=float(b)
                        if a < 0 or b<0 or  a==1:
                            raise Exception
                        print('log=' + str(log(b,a)))
                        break
                    except Exception:
                        print('Uncorrect data!')
            elif n == '3':
                while True:
                    b = input('Enter b calculation of 10-logarithm : ')


                    try:

                        b = float(b)
                        if b < 0 :
                            raise Exception
                        print('lg=' + str(log(b,10)))
                        break
                    except Exception:
                        print('Uncorrect data!')
            else:
                raise Exception
            break

        except Exception:
            print('Uncorrect data!')


