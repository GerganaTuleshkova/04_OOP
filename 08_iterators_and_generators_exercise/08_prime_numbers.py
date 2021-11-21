def get_primes(given_list):
    for n in given_list:
        is_prime = True
        if n < 1:
            is_prime = False
            break
        for delimiter in range(2, n):
            if n % delimiter == 0:
                is_prime = False
                break
        if is_prime:
            yield n


print(list(get_primes([-2, 0, 0, 1, 1, 0])))

