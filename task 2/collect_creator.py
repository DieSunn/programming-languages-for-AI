__author__ = "Sizikov A.S."

from random import randint
import numpy as np
from write_to_file import write_to_csv
from timer import timer

@timer
def list_creator(n: int, a: int, b: int, filename: str = 'list_collection_output.csv') -> None:
    """
    Создайте набор из случайных чисел без повторов x1, x2, ..., xn, используя list. \n 
    Интервал (a,b) и количество случайных чисел задаются пользователем. n << b−a\n
    Нечётный вариант: набор из их нечётных чисел.

    :param n: Размер создаваемой коллекции.
    :type n: int
    :param a: Начало интервала.
    :type a: int
    :param b: Конец интервала.
    :type b: int
    :return: Возвращает список состоящий из случайных чисел без повторов.
    """

    data = []

    if b < a or (n > b - a):
        return "Неподходящий интервал по условию задачи"
    if n < 0:
        return "Неверное значение n"
    
    while True:
        num = randint(a, b)
        if num not in data and num % 2 != 0:
            data.append(num) 
        
        if len(data) == n:
            break

    return data


@timer
def set_creator(n: int, a: int, b: int, filename: str = 'set_collection_output.csv') -> list:
    """
    Создайте набор из случайных чисел без повторов x1, x2, ..., xn, используя set. \n 
    Интервал (a,b) и количество случайных чисел задаются пользователем. n << b−a\n
    Нетный вариант: набор из их нечётных чисел.
    
    :param n: Размер создаваемой коллекции.
    :type n: int
    :param a: Начало интервала.
    :type a: int
    :param b: Конец интервала.
    :type b: int
    :return: Возвращает множество состоящее из случайных чисел без повторов.    
    """

    data = set()

    if b < a or (n > b - a):
        return "Неподходящий интервал по условию задачи"
    if n < 0:
        return "Неверное значение n"
    
    while True:
        if (num:=randint(a, b)) % 2 != 0:
            data.add(num)

        if len(data) == n:
            break

    data = list(data)

    return data


@timer
def numpy_ndarray_collection(n: int, a: int, b: int, filename: str = 'ndarray_collection_output.csv') -> np.ndarray:
    """
    Создайте набор из случайных чисел без повторов x1, x2, ..., xn, используя ndarray из numpy. \n 
    Интервал (a,b) и количество случайных чисел задаются пользователем. n << b−a\n
    Нетный вариант: набор из их нечётных чисел.
    
    :param n: Размер создаваемой коллекции.
    :type n: int
    :param a: Начало интервала.
    :type a: int
    :param b: Конец интервала.
    :type b: int
    :return: Возвращает множество состоящее из случайных чисел без повторов.    
    """

    
    if b < a or (n > b - a):
        return "Неподходящий интервал по условию задачи"
    if n < 0:
        return "Неверное значение n"

    nums = np.arange(a, b+1)
    nums = nums[nums % 2 != 0]

    data = np.random.choice(nums,
                            n,
                            replace=False)
    
    return data