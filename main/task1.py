__author__ = "Sizikov A.S."

def solution() -> None:
    """Ввести с клавиатуры координаты точек A и В.\n
    Определить, какая из точек наименее удалена от начала координат.
    """

    print("Введите координаты точки A (формат вводимых координат - 2 2)")
    A: list[int] = map(int, input("Точка A = ").split())

    print("\nВведите координаты точки B")
    B: list[int] = map(int, input("Точка B = ").split())
    
    A_len: float = (next(A)**2 + next(A)**2)**.5
    B_len: float = (next(B)**2 + next(B)**2)**.5

    print(f"\nДлина вектора OA - {A_len:.2f};\nДлина вектора OB - {B_len:.2f};\n")

    print("Вектор OB ближе к началу координат, чем OА") if A_len > B_len else print("Вектор OB ближе к началу координат, чем OА")
