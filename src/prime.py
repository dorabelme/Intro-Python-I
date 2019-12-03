import sys
import math

# print(sys.argv)
input_number = int(sys.argv[1])


def is_prime_bruteforce(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_prime_optimized(number):
    if number <= 1:
        return False

    for i in range(2, int(math.ceil(math.sqrt(number)))+1):
        if number % i == 0:
            return False

    return True


def is_prime_recursion(number):
    if number <= 1:
        return False

    def is_prime(divisor, number):
        if divisor == 1:
            return True
        elif number % divisor == 0:
            return False
        else:
            return is_prime(divisor-1, number)

    return is_prime(number-1, number)


def sieve_solution(number):
    primeArray = [True for x in range(2, number + 1)]
    primes = []

    for i in range(len(primeArray)):
        is_prime = primeArray[i]

        if is_prime:
            primes.append(i+2)

            for j in range(i * 2 + 2, len(primeArray), i + 2):
                primeArray[j] = False

    return primes


output1 = is_prime_bruteforce(input_number)
output2 = is_prime_recursion(input_number)
output3 = is_prime_optimized(input_number)
output4 = sieve_solution(input_number)

print(output1, output2, output3)
print(output4)
