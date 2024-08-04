from typing import List, Any
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
    # if count > len(arr) and repeat is False:
    #     raise NegativeError("Значение `count` не должно превышать количество элементов `arr`")
    
    # arr = mix_array(arr)
    # new_arr = []
    # for _ in range(count):
    #     def random_selection_func(arr):
    #         arrCopy = arr.copy()
    #         while len(arrCopy) > 1:
    #             n = len(arrCopy)
    #             mid = n // 2
    #             arrCopy = random_simple([arr[:mid], arr[mid:]])[0]
    #         if repeat is False:
    #             if arrCopy[0] not in new_arr:
    #                 new_arr.append(arrCopy[0])
    #             else:
    #                 while arrCopy[0] in new_arr:
    #                     arrCopy = random_selection_func(arr)
    #         else:
    #             new_arr.append(arrCopy[0])
    # return new_arr

    if count > len(arr) and not repeat:
        raise NegativeError("Значение `count` не должно превышать количество элементов `arr`")

    arr = mix_array(arr)
    new_arr = []

    for _ in range(count):
        def random_selection_func(arr):
            arr_copy = arr.copy()
            while len(arr_copy) > 1:
                n = len(arr_copy)
                mid = n // 2
                arr_copy = random_simple([arr_copy[:mid], arr_copy[mid:]])
            return arr_copy[0]

        selected_item = random_selection_func(arr)
        
        if repeat:
            new_arr.append(selected_item)
        else:
            while selected_item in new_arr:
                selected_item = random_selection_func(arr)
            new_arr.append(selected_item)

    return new_arr

