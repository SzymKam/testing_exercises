def number_is_prime(number: int) -> bool:
    if number == 2:
        return True
    if number % 2 == 0 or number <= 1:
        return False
    prime = int(number**0.5) + 1
    for divider in range(3, prime, 2):
        if number % divider == 0:
            return False
    return True