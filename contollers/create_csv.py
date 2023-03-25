import csv


def create_table(field_names: list, filename: str, write_rows: list[dict]):
    """
    Создать csv таблицу
    :param field_names: поля заголовков
    :param filename: Имя файла
    :param write_rows: данные в формате [{'name': name, 'professions': professions, 'email': email}]
    """

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(write_rows)
