# version 1.0.0
# Программа для проверки на простое число

import json
import os

def check_cache(n: int):
    """
    Функция для проверки кэша на наличие проверяемого числа.

    Args:
        n [int]: это натуральное число, которое будет проверяться.

    Return:
        [None]: отсутствие числа или файла.
        [bool]: результат проверки на простоту из кэша.
    """
    try:
        if os.path.isfile("cache.json"):
            with open("cache.json", "r") as f:
                content = f.read().strip()
                if not content:
                    return None
                cache = json.loads(content)
                return cache.get(str(n))
        else:
            with open("cache.json", "w") as f:
                json.dump({}, f)
            return None
    except json.JSONDecodeError:
        os.remove("cache.json")
        with open("cache.json", "w") as f:
                json.dump({}, f)
        return None

def update_cache(n: int, result: bool) -> None:
    """
    Функция для добавления данных в кэш.

    Args:
        n [int]: это натуральное число, которое будет проверяться.
        result [bool]: это результат проверки числа на простоту.

    Return:
        [None]: функция ничего не возвращает
    """

    cache = {}

    with open("cache.json", "r") as f:
        content = f.read()
        if content:
            cache = json.loads(content)

    cache[str(n)] = result

    with open("cache.json", "w") as f:
        json.dump(cache, f, indent=4)

def is_prime(n: int) -> bool:
    """
    Проверяет число на простоту.
    
    Args:
        n [int]: это натуральное число, которое будет проверяться.

    Return:
        [bool]: результат проверки.
    """

    if n < 2:
        return False
    
    cached_result = check_cache(n)
    if cached_result is not None:
        return cached_result
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            update_cache(n, False)
            return False
    update_cache(n, True)
    return True

def output(result: bool) -> str:
    """
    Описывает результат программы.
    
    Args:
        result [bool]: это результат проверки на простоту.

    Return:
        [str]: это описание результата.
    """

    if result:
        return "Число является простым"
    else:
        return "Число является составным"
    
def main():
    """
    Главная функция программы.
    """
    try:
        number = int(input())
        result = is_prime(number)
        print(output(result))
        input()
    except ValueError:
        print("Введено некорректное число. Пожалуйста, введите натуральное число.")


if __name__ == "__main__":
    main()
