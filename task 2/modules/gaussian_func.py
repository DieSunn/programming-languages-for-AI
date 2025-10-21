__author__ = "Sizikov A.S."

import numpy as np


def read_data(filename: str) -> map:
    """
    Функция записывает значения из текстового файла и возвращает
    список целочисленных чисел

    :param filename: Название текстового файла, из которого будут взяты значения
    :type filename: str
    """
    with open(f"./output/{filename}", 'r') as file:
        data = map(int, file.readlines())
    
    return data

def gauss(x) -> np.float64:
    """
    Возвращает результат функции Гаусса

    :param x: Число для рассчета
    :type x: int
    """
    return np.exp(-x**2)

def calculate_gaussian_function(data) -> np.ndarray:
    """
    Функция принимает набор из значении и возвращает список 
    из обработанных функцией Гаусса значений
    :param data: Набор целочисленных значений
    """
    data_list = np.array(data)
    return gauss(data_list)