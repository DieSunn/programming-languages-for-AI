__author__ = "Sizikov A.S."

from modules.collect_creator import *
from modules.gaussian_func import read_data, calculate_gaussian_function


def main(*args, **kwargs):
    """
    Создайте набор из случайных чисел без повторов x1, x2, ..., xn.\n 
    Интервал (a,b) и количество случайных чисел задаются пользователем. n << b−a\n
    Нечётный вариант: набор из их нечётных чисел.
    """

    question = input("Ввести значения через консоль? (y/n) ")
    if question == "y":
        n = int(input())
        a = int(input())
        b = int(input())
    else:
        n = 10**6     #Размер набора чисел
        a = 0       #Начальное значение интервала
        b = 10**7   #Конечное значение интервала

    # list_collection = list_creator(n, a, b)
    # set_collection = set_creator(n, a, b)
    ndarray_collection = numpy_ndarray_collection(n, a, b)

    write_to_csv("output", 
                           ndarray_collection=ndarray_collection)
    print("Данные записаны в файлы\n")

    data = calculate_gaussian_function(ndarray_collection)
    data = np.prod(data)

    print(f"Произведение значений, обработанных функции Гаусса, равняется {data}")


if __name__ == "__main__":
    main()