import numpy as np


def gaussian_function(x) -> float:
    return np.exp(-x**2)


def read_data(filename: str):
    with open(filename, 'r') as file:
        data = map(int, file.readlines())
    
    return data


def calculate_gaussian_function(data) -> list:
    data = map(gaussian_function, data)
    return list(data)


