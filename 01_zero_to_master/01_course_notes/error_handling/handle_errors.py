
while True:
    try:
        age = int(input('Enter your age: '))
        print(10/age)
    except ValueError as err:
        print(f'We need a number here. {err}')
    except ZeroDivisionError as err:
        print(f'Enter value higher than 0. {err}')
    else:
        print('Thank you')
        break
    finally:
        print('This always is executed')
