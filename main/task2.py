__author__ = "Sizikov A.S."

from random import randint


def solution() -> None:
    """
    Билет называют счастливым, если в его номере сумма первых трех цифр равна сумме последних трех.\n
    Подсчитать число тех "счастливых" билетов, у которых сумма трех цифр равна 13.
    Номер билета может быть от 000000 до 999999
    """
    
    count:str = 0
    
    for i in range(1_000_000):
        ticket: str = str(i).rjust(6, '0')
        first_part: int = sum(map(int, ticket[:3]))
        second_part: int = sum(map(int, ticket[3:]))

        if (first_part == second_part) and first_part == 13:
            count += 1

    print(f'Количество "счастливых" билетов, у которых сумма трех цифр равны 13 - {count}')

