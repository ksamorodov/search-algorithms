def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def fibonacci_search(arr, target):
    fib_minus_2 = 0
    fib_minus_1 = 1
    fib = fib_minus_1 + fib_minus_2

    while fib < len(arr):
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
        fib = fib_minus_1 + fib_minus_2

    offset = -1

    while fib > 1:
        i = min(offset + fib_minus_2, len(arr) - 1)

        if arr[i] < target:
            fib = fib_minus_1
            fib_minus_1 = fib_minus_2
            fib_minus_2 = fib - fib_minus_1
            offset = i
        elif arr[i] > target:
            fib = fib_minus_2
            fib_minus_1 = fib_minus_1 - fib_minus_2
            fib_minus_2 = fib - fib_minus_1
        else:
            return i

    if fib_minus_1 and arr[offset + 1] == target:
        return offset + 1

    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0

    size = len(arr)
    i = 1

    while i < size and arr[i] <= target:
        i *= 2

    return binary_search(arr, target, i // 2, min(i, size - 1))


# Пример использования:

# Ввод массива чисел
numbers = input("Введите числа через пробел: ").split()
arr = [int(num) for num in numbers]

# Ввод целевого элемента
target = int(input("Введите целевой элемент: "))

# Выбор вида поиска
search_type = input("Выберите вид поиска: (линейный/бинарный/фибоначчи/экспоненциальный) ")

# Выполнение выбранного вида поиска
if search_type == "линейный":
    index = linear_search(arr, target)
elif search_type == "бинарный":
    arr.sort()  # Бинарный поиск требует отсортированного массива
    index = binary_search(arr, target)
elif search_type == "фибоначчи":
    arr.sort()  # Поиск Фибоначчи также требует отсортированного массива
    index = fibonacci_search(arr, target)
elif search_type == "экспоненциальный":
    arr.sort()  # Экспоненциальный поиск требует отсортированного массива
    index = exponential_search(arr, target)
else:
    print("Неверно выбран вид поиска.")
    exit()

# Вывод результата
if index != -1:
    print("Элемент найден. Индекс:", index)
else:
    print("Элемент не найден.")
