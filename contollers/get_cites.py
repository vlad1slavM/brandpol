import json


def get_city_names(filename: str) -> list:
    """
    Получить названия городов из json файла
    :param filename: имя файла
    """
    names = []
    f = open(filename)
    file = json.load(f)
    for city in file:
        names.append(city.get('name'))
    f.close()
    return names
