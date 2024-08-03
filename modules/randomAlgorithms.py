from typing import List, Any
import random


class randomAlgorithms:
    """ Класс случайных алгоритмов.
    Содержит алгоритмы, которые усиливают случайность
    выпадения элемента или элементов.

    - Разбиение списка на несколько частей (3) и случайный
      выбор каждой, рекурсивно, пока размер не станет 1.

    - Перемешка списка и выбор случайного элемента из него.
    """

    
    
    def random_element(arr: List, count: int = 1) -> List:
        """ Выбор случайных элементов из списка.
        Возвращает список из случайного элемента или
        элементов.

        Передаваемые аргументы:
        arr -- список
        count -- количество элементов, которое нужно возвращать
        """
    
        newArr = []
        for _ in range(count):
            random_element = random.choice(arr)
            newArr.append(random_element)
            arr.remove(random_element)
        return newArr

    def mix_array(arr: List) -> List:
        """ Перемешивание списка.
        Возвращает случайно перемешанный список.

        Передаваемые аргументы:
        arr -- список для перемешки
        """
        # newArr = []
        # arrCopy = arr.copy()
        # for _ in range(len(arrCopy) + 1):
        #     random_element = random.choice(arrCopy)
        #     newArr.append(random_element)
        #     arrCopy.remove(random_element)
        return random.shuffle(arr.copy())


        # for _ in range(len(arr) + 1):
        #     n = len(arr)
        #     if n == count:
        #         break
        #     noise_level = random.uniform(-0.3, 0.3)
        #     index = int((n - 1) * (random.random() + noise_level))
        #     index = max(0, min(n - 1, index))
        #     arr.pop(index)
        #     newArr.append(arr[index])

        # return newArr
    
print(randomAlgorithms.random_element([1,2,3,4,5,6,7,8,9,10,0],12))