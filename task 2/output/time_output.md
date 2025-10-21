# Время выполнения
- Finished set_creator                                        in 0.0001 seconds 
- Finished numpy_ndarray_collection                           in 0.0265 seconds
- Finished list_creator                                       in 0.0001 seconds
- Finished set_creator                                        in 0.0000 seconds
- Finished numpy_ndarray_collection                           in 0.0299 seconds
- Finished list_creator                                       in 0.0001 seconds
- Finished set_creator                                        in 0.0001 seconds
- Finished numpy_ndarray_collection                           in 0.0243 seconds
- Finished list_creator                                       in 1.0822 seconds
- Finished set_creator                                        in 0.0179 seconds
- Finished numpy_ndarray_collection                           in 0.0306 seconds
- Finished list_creator                                       in 0.0001 seconds
- Finished set_creator                                        in 0.0000 seconds
- Finished numpy_ndarray_collection                           in 0.0219 seconds
- Finished list_creator                                       in 0.0001 seconds
- Finished set_creator                                        in 0.0000 seconds
- Finished numpy_ndarray_collection                           in 0.0266 seconds
- Finished numpy_ndarray_collection                           in 0.0236 seconds
- Finished numpy_ndarray_collection                           in 8.7178 seconds
- Finished numpy_ndarray_collection                           in 0.5201 seconds
- Finished numpy_ndarray_collection                           in 0.5860 seconds

# Отчёт

- list_creator: Быстро работает только на малых объёмах, но при увеличении размера коллекции резко теряет производительность из-за медленного поиска уникальных элементов в списке.<br>
Сложность: O(n<sup>2</sup>).

- set_creator: Обычно работает быстрее списка за счёт быстрого поиска уникальности во множестве, но при большом количестве попыток (особенно при большом n) также может замедляться.<br>
Сложность: O(n)

- numpy_ndarray_collection: Самый быстрый и эффективный способ для малых и средних диапазонов благодаря векторизации и оптимизации NumPy. Однако при очень больших диапазонах может потреблять много памяти, поэтому для них используется генерация через set.<br>
Сложность: 
    - O(n*m), где n - набор нечетных чисел при малом количестве чисел;
    - O(n<sup>2</sup>), где n - набор нечетных чисел при малом количестве чисел.


# Вывод

Для небольших коллекций разница в скорости незначительна, но при увеличении объёма данных предпочтительнее использовать NumPy или set, так как они обеспечивают лучшую производительность и масштабируемость.