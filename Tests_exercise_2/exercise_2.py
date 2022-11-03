from typing import Union


def fizz_buzz(number: int) -> Union[str, int]:

    if number == 0:
        return 0
    elif number % 5 == 0 and number % 3 == 0:
        return 'fizzbuzz'
    elif number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    else:
        return 0
