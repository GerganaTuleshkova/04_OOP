def is_prime(n):
    is_prime_number = True
    if n <= 1:
        return False
    for delimiter in range(2, n):
        if n % delimiter == 0:
            is_prime_number = False
            break
    return is_prime_number


def get_primes(given_list):
    for n in given_list:
        if is_prime(n):
            yield n


print(list(get_primes([-2, 0, 0, 1, 1, 0])))

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

