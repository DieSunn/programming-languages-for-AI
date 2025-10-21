__author__ = "Sizikov A.S."

import csv

def write_to_csv(file_prefix: str, **datasets) -> None:
    """
    Функция записывает данные в csv-файлы.

    :param file_prefix: Префикс для названий файлов
    :type file_prefix: str
    :param datasets: Наборы данных (ключ — имя, значение — коллекция)
    """
    for name, data in datasets.items():
        filename = f"./output/{file_prefix}_{name}.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in data:
                # если число -> упакуем в список
                if not isinstance(row, (list, tuple, set)):
                    csv_writer.writerow([row])
                else:
                    csv_writer.writerow(row)


def write_to_md(func_name: str, run_time: float, filename: str = "time_output.md"):
    """
    Функция записывает данные в md-файл
    """
    with open(f"./output/{filename}", "a") as md_file:
        md_file.write(f"Finished {func_name:50s} in {run_time:.4f} seconds\n")