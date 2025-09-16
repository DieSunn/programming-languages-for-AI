import pytest
import numpy as np
import os
from gaussian_func import gaussian_function, read_data, calculate_gaussian_function

def test_gaussian_function_zero():
    assert gaussian_function(0) == pytest.approx(1.0)

def test_gaussian_function_positive():
    assert gaussian_function(1) == pytest.approx(np.exp(-1))

def test_gaussian_function_negative():
    assert gaussian_function(-2) == pytest.approx(np.exp(-4))

def test_calculate_gaussian_function():
    data = [0, 1, -1]
    result = calculate_gaussian_function(data)
    expected = [np.exp(-x**2) for x in data]
    assert result == pytest.approx(expected)

def test_read_data(tmp_path):
    # Создаём временный файл с числами
    file_path = tmp_path / "test.txt"
    file_content = "1\n2\n-3\n"
    file_path.write_text(file_content, encoding="utf-8")
    data = list(read_data(str(file_path)))
    assert data == [1, 2, -3]