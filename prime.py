# version 0.0.1
# Программа для проверки на простое число

number = int(input())

def is_prime(n):
    if n < 2:
        return f"{n} это не натуральное число"
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

result = is_prime(number)
print(result)
