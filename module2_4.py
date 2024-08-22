num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
is_prime = True
for i in num:
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
        else:not_prime.append(i)
        is_prime = True
print(prime)
print(not_prime)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# is_prime = True
#
# for number in numbers:
#     if number > 1:
#         for i in range(2, number):
#             if (number % i) == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(number)
#         else:
#             not_primes.append(number)
#         is_prime = True
#
# print(primes)
# print(not_primes)