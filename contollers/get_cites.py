import json


def get_city_names(filename: str) -> list:
    """
    Получить названия городов из json файла
    :param filename: имя файла
    """
    names = []
    with open(filename) as file:
        file = json.load(file)
    for city in file:
        names.append(city.get('name'))
    return names
