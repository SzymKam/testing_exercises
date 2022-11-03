import time


def calc_power(base: [int, float], exp: [int, float]) -> [int, float]:
    return base ** exp


def calc_sum_arith_seq(start: int, end: int) -> int:
    result = 0
    for element in range(start, end + 1):
        result += element
    return result


def do_calculation(value: int) -> int:
    response = call_api()
    return response + value


def call_api() -> int:
    time.sleep(10)
    return 100
