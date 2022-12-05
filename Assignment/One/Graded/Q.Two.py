def Goldbach(n):

    prme = []
    gold = []

    for i in range(2, n):
        print(i, prime(i))
        if (prime(i)):
            prme.append(i)

    prme = sorted(prme)
    print(prme)

    for x in range(len(prme)):
        for y in range(x, len(prme)):
            if prme[x] + prme[y] == n:
                gold.append((prme[x], prme[y]))

    print(gold)


def prime(n):
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
            break
    return result


Goldbach(16)
