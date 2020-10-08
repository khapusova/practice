r=int(input('enter your rating score:'))
if r>=0 and r<=59:
    print('Your mark is Unsatisfactory')
elif  r>=60 and r<=64:
    print('Your mark is Marginal')
elif  r>=65 and r<=74:
    print('Your mark is     Satisfactory')
elif  r>=75 and r<=84:
    print('Your mark is Good')
elif  r>=85 and r<=94:
    print('Your mark is Very good')
elif  r>=95 and r<=100:
    print('Your mark is Excellent')
else:
    print('Error! You wrote a wrong number.')

