__author__ = "Sizikov A.S."

from collect_creator import *

def main(*args, **kwargs):
    """
    Создайте набор из случайных чисел без повторов x1, x2, ..., xn.\n 
    Интервал (a,b) и количество случайных чисел задаются пользователем. n << b−a\n
    Нечётный вариант: набор из их нечётных чисел.
    """

    question = input("Ввести значения через консоль? (y/n)")
    if question == "y":
        n = int(input())
        a = int(input())
        b = int(input())
    else:
        n = 10**6  #Размер набора чисел
        a = 0       #Начальное значение интервала
        b = 10**10   #Конечное значение интервала

    list_collection = list_creator(n, a, b)
    set_collection =  set_creator(n, a, b)
    ndarray_collection = numpy_ndarray_collection(n, a, b)

    write_to_csv("output", list_collection=list_collection,
                           set_collection=set_collection,
                           ndarray_collection=ndarray_collection)

if __name__ == "__main__":
    main()