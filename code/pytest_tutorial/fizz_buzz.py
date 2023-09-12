def fizz_buzz(number):
    if number == 0:
        result = number
    elif not number % 3 and not number % 5:
        result = 'FizzBuzz'
    elif not number % 3:
        result = 'Fizz'
    elif not number % 5:
        result = 'Buzz'
    else:
        result = number
    return result


if __name__ == '__main__':
    for n in range(20):
        print(fizz_buzz(n))
