__author__ = "Sizikov A.S."

import pytest
import numpy as np
import os
from .__init__ import gauss, calculate_gaussian_function

def test_gaussian_function_zero():
    """При 0 функция Гаусса равняется 0"""
    assert gauss(0) == pytest.approx(1.0)

def test_gaussian_function_positive():
    """При 1 функция Гаусса равняется 1/е"""
    assert gauss(1) == pytest.approx(np.exp(-1))

def test_gaussian_function_negative():
    """При 1 функция Гаусса равняется 1/е^4"""
    assert gauss(-2) == pytest.approx(np.exp(-4))

def test_calculate_gaussian_function():
    """Проверка значений при наборе данных"""
    data = [0, 1, -1]
    result = calculate_gaussian_function(data)
    expected = [np.exp(-x**2) for x in data]
    assert result == pytest.approx(expected)

