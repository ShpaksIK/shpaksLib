from typing import List
import random


class NegativeError(Exception): ...


""" Модуль случайных алгоритмов.
Содержит алгоритмы, которые усиливают случайность
выпадения элемента или элементов.

- Разбиение списка на несколько частей (3) и случайный
    выбор каждой, рекурсивно, пока размер не станет 1.
"""

def mix_array(arr: List) -> List:
    """ Перемешивание списка.
    Возвращает случайно перемешанный список.

    Передаваемые аргументы:
    arr -- список для перемешки
    """
    new_arr1 = []
    new_arr2 = []
    arrCopy = arr.copy()

    for _ in range(len(arrCopy)):
        random_element = random.choice(arrCopy)
        new_arr1.append(random_element)
        arrCopy.remove(random_element)

    for _ in range(len(new_arr1)):
        n = len(new_arr1)
        noise_level = random.uniform(-0.3, 0.3)
        index = int((n - 1) * (random.random() + noise_level))
        index = max(0, min(n - 1, index))
        new_arr2.append(new_arr1[index])
        new_arr1.pop(index)

    return new_arr2

def random_simple(arr: List, count: int = 1, repeat: bool = False) -> List:
    """ Выбор случайных элементов из списка.
    Возвращает список из случайного элемента или
    элементов.

    Передаваемые аргументы:
    arr -- список
    count -- количество элементов, которое нужно возвращать
    repeat -- могут ли допускаться повторения случайных
    элементов (по уполчанию False)
    """
    if count > len(arr) and repeat is False:
        raise NegativeError("Значение `count` не должно превышать количество элементов `arr`")
    
    mixed_arr = mix_array(arr)
    new_arr = []

    for _ in range(count):
        random_element = random.choice(mixed_arr)
        new_arr.append(random_element)
        if repeat is False:
            mixed_arr.remove(random_element)

    return new_arr

def random_selection(arr: List, count: int = 1, repeat: bool = False) -> List:
    """ Выбор случайных элементов из списка.
    Возвращает список из случайного элемента или
    элементов.
    Данный алгоритм разделяет список на 2 части и
    выбирает случайную из них, пока не останется 1 элемент.

    Передаваемые аргументы:
    arr -- список
    count -- количество элементов, которое нужно возвращать
    repeat -- могут ли допускаться повторения случайных
    элементов (по уполчанию False)
    """
    if count > len(arr) and repeat is False:
        raise NegativeError("Значение `count` не должно превышать количество элементов `arr`")

    if count == len(arr) and repeat is False:
        return mix_array(arr)

    def random_selection_func(arr_temp):
        global side
        if len(arr_temp) > 1:
            mid = len(arr_temp) // 2
            side = random.choice([arr_temp[:mid], arr_temp[mid:]])
            random_selection_func(arr_temp=side)
        return side
    
    new_arr = []
    for _ in range(count):
        if repeat:
            new_arr.append(random_selection_func(arr_temp=arr)[0])
        else:
            random_element = random_selection_func(arr_temp=arr)[0]
            arr.remove(random_element)
            new_arr.append(random_element)

    return new_arr
