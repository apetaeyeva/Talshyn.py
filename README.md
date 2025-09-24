numbers = [3.5, 8, -2, 7, 10, 15, 6, 4, 9, 12]

even_numbers = [x for x in numbers if x % 2 == 0]
if even_numbers:
    max_even = max(even_numbers)
    print("Максимум среди четных элементов:", max_even)
else:
    print("Четных элементов нет")
