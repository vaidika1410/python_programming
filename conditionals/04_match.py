a = int(input('enter a number between 1 and 10: '))

match a:
    case 1:
        print('you won a prize of camera')
    case 5:
        print('you won a TV')
    case 4:
        print('you won a prize of $10')
    case _:
        print('Oops! better luck next time')