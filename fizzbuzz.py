def fizz_buzz(int_value):
    count = 1
    if int_value <= 0:
        print('Value should start at 1')
    else:
        while count <= int_value:
            answer = ''
            if count % 3 == 0:
                answer = f'{answer}Fizz'
                if count % 5 == 0:
                    answer = f'{answer}Buzz'
                if count % 5 != 0 and count % 3 != 0:
                    answer = count

            count += 1
            print(answer)


try:
    fizz_buzz(int(input('Enter a number: ')))
except ValueError:
    print('Input error: value entered is not integer')
