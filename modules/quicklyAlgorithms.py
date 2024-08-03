from typing import List, Callable
from functools import wraps
from time import time


class NegativeError(Exception): ...


""" Названия функций.
Группировка функций по наличию аргументов:
0: list
1: list, int
"""
funcs_by_args = (("selection_sort", "quick_sort", "smallest_search", "biggest_search"), ("binary_search"))


def check_isinstance(func: Callable) -> Callable:
    """ Проверка типов аргументов.
    Функция, вызывающаяся при выполнении методов класса.
    Проверяет тип данных аргументов.
    """
    def wrapper(*args):

        if func.__name__ in funcs_by_args[0]:
            if not isinstance(args[0], list):
                raise NegativeError("Передаваемый арнумент 'arr' не является списком.")
            
        elif func.__name__ in funcs_by_args[1]:
            if not isinstance(args[0], list):
                raise NegativeError("Передаваемый арнумент 'arr' не является списком.")
            if not isinstance(args[1], int):
                raise NegativeError("Передаваемый арнумент 'item' не число")
            
        return func(*args)
    return wrapper


def time_execution(func: Callable) -> Callable:
    """ Подсчет времени выполнения функции.
    Функция, вызывающаяся при выполнении методов класса
    и подсчитывающая время выполнения данного метода.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        execution_time = end_time - start_time

        show_time = kwargs.get('show_time', False)
        if show_time:
            return execution_time, result
        return result
    
    return wrapper


class quicklyAlgorithms:
    """ Класс алгоритмов.
    Множество видов алгоритмов представленно в этом классе:
    - Сортировки (выбором, быстрая...)
    - Поиск (бинарный, наименьшего, наибольшего...)

    Большинство методов содержат параметр show_time (по умолчанию False).
    При значении True функция возвращает время выполнения метода и результат
    в виде кортежа: (execution_time, result).
    """
    
    @staticmethod
    @time_execution
    @check_isinstance
    def selection_sort(arr: List, how_sort: str = "up", show_time: bool = False) -> List[int]: 
        """ Алгоритм сортировки выбором.
        Возвращает отсортированный список по возрастанию
        (по умолчанию) или по убыванию.
        Может работать со списками из чисел или из букв.

        Передаваемые аргументы:
        arr -- список для сортировки (численный или буквенный)
        how_sort -- как сортировать (up по умолчанию): 
                    up - по возрастанию,
                    down - по убыванию
        show_time -- возвращать время выполнения функции (по умолчанию False)
        """
        newArr = []
        for _ in range(len(arr)):
            if how_sort == "up":
                smallest = quicklyAlgorithms.smallest_search(arr)
            elif how_sort == "down":
                smallest = quicklyAlgorithms.biggest_search(arr)
            else:
                raise NegativeError("Аргумент 'how_sort' должен принимать либо up, либо down.")
            newArr.append(arr.pop(smallest))
        return newArr

    @staticmethod
    @time_execution
    @check_isinstance
    def quick_sort(arr: List[int], show_time: bool = False) -> List[int]:
        """ Алгоритм быстрой сортировки.
        Возвращает отсортированный список по возрастанию.
        Данный алгоритм работает быстрее, чем сортировка выбором.

        Передаваемые аргументы:
        arr -- численный список для сортировки
        show_time -- возвращать время выполнения функции (по умолчанию False)
        """
        # Быстрая сортировка через рекурсию
        # if len(arr) < 2:
        #     return arr
        # else:
        #     pivot = arr[0]
        #     less = [i for i in arr[1:] if i <= pivot]
        #     greater = [i for i in arr[1:] if i > pivot]
        #     return quicklyAlgorithms.quick_sort(less) + [pivot] + quicklyAlgorithms.quick_sort(greater)

        def quick_sort_big(arr):
            """ Алгоритм быстрой сортировки для больших списков. """
            stack = []
            stack.append((0, len(arr) - 1))
            while stack:
                start, end = stack.pop()
                if start < end:
                    pivot_index = partition(arr, start, end)
                    stack.append((start, pivot_index - 1))
                    stack.append((pivot_index + 1, end))
            return arr

        def partition(arr, start, end):
            pivot = arr[end]
            i = start - 1
            for j in range(start, end):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[end] = arr[end], arr[i + 1]
            return i + 1
        
        return quick_sort_big(arr)

    @staticmethod
    @time_execution
    @check_isinstance
    def binary_search(arr: List[int], item: int, show_time: bool = False) -> int:
        """ Алгортим бинарного поиска.
        Аргумент arr принимает только отсортированный по возврастанию список.
        Возвращает индекс искомого item, в противном случае None.

        Передаваемые аргументы:
        arr -- численный список для поиска
        item -- число, которое нужно найти
        show_time -- возвращать время выполнения функции (по умолчанию False)
        """
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = arr[mid]
            if guess == item:
                return mid
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
        return None

    @staticmethod
    @time_execution
    @check_isinstance   
    def smallest_search(arr: List, show_time: bool = False) -> int | str:
        """ Алгоритм нахождения наименьшего значения.
        Возвращает индекс наименьшего значения.
        Может принять числовой список и вернуть индекс наименьшего числа.
        Может принять символьный список и вернуть индекс наименьшего символа.

        Передаваемые аргументы:
        arr -- список для поиска (численный или буквенный)
        show_time -- возвращать время выполнения функции (по умолчанию False)
        """
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest_index = i
                smallest = arr[i]      
        return smallest_index
    
    @staticmethod
    @time_execution
    @check_isinstance
    def biggest_search(arr: List, show_time: bool = False) -> int | str:
        """ Алгоритм нахождения наибольшего значения.
        Возвращает индекс наибольшего значения.

        Передаваемые аргументы:
        arr -- список для поиска (численный или буквенный)
        show_time -- возвращать время выполнения функции (по умолчанию False)
        """
        smallest = arr[0]
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] > smallest:
                smallest_index = i
                smallest = arr[i]      
        return smallest_index
