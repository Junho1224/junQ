m = int(input())
n = int(input())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(m, n):
    primes = []
    for num in range(m, n + 1):
        if is_prime(num):
            primes.append(num)
    # print(primes)
    return primes



result = find_primes(m, n)


if len(result) ==0:
    print(-1) 
else:
    print(sum(result))
    print(min(result))
