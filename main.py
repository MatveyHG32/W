countries = ["Украина", "Монголия", "Афганистан", "Россия"]

coords = [
    (50.45, 30.52),
    (47.92, 106.92),
    (34.53, 69.17),
    (55.75, 37.62)
]


# Функция создания словаря
def make_dict(countries, coords):

    result = {}

    for i in range(len(countries)):
        result[countries[i]] = coords[i]

    return result


# Функция тестов
def tests():

    data = make_dict(countries, coords)

    # сравнение значений
    assert data["Украина"] == (50.45, 30.52)
    assert data["Монголия"] == (47.92, 106.92)
    assert data["Афганистан"] == (34.53, 69.17)
    assert data["Россия"] == (55.75, 37.62)

    #тест 1
    assert len(data) == 4

    #тест2
    assert data["Украина"] == coords[0]

    # нерабочий тест (закомментирован)
    # assert data["Россия"] == (0, 0)

    print("Все тесты прошли!")


country_data = make_dict(countries, coords)

print(country_data)

tests()