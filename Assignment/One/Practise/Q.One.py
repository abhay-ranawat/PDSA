def Twin_Primes(n, m):

    prime_list = []
    twin_prime = []

    for i in range(n, m+1):

        if prime(i):
            prime_list.append(i)

    prime_list = sorted(prime_list)

    for i in range(len(prime_list)-1):

        if ((prime_list[i+1] - prime_list[i]) == 2):
            twin_prime.append((prime_list[i], prime_list[i+1]))

    return twin_prime


def prime(n):
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
            break
    return result


print(Twin_Primes(5, 50))
