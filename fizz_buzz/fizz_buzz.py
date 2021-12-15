def fizz_buzz(num: int) -> int or str:

    if num % 3 == 0:
        return 'fizz'

    return num


if __name__ == '__main__':

    while True:
        input_data = input('Write a number: ')

        try:
            input_number = int(input_data)

        except ValueError:
            print(f'{input_data} is not valid data. Try again')

        else:
            result = fizz_buzz(input_number)
            print(result)
            break
