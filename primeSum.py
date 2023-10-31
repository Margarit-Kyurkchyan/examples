def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sum_primes_except_ending_in_3(start, end):
    total = 0
    for num in range(start, end + 1):
        if is_prime(num) and num % 10 != 3:
            total += num
    return total


start_range = 5
end_range = 10000  # 10 million

result = sum_primes_except_ending_in_3(start_range, end_range)
print("Sum of primes from", start_range, "to", end_range, "excluding primes ending in 3:", result)
