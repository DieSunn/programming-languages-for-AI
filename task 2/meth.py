from math import exp

def gaussian_function(x) -> float:
    return exp(-x**2)

    

def read_data(filename: str):
    with open(filename, 'r') as file:
        data = map(int, file.readlines())
    
    return data

def calculate_gaussian_function(filename: str = 'ndarray_collection_output.csv'):
    data = read_data(filename)
    data = map(gaussian_function, data)

    print(list(data))

calculate_gaussian_function()