import os


# Представление файла recipes.txt в виде словаря
def file_to_dict():
    path = os.path.join(os.getcwd(), 'Recipes.txt')
    with open(path, 'r', encoding = 'utf-8') as cook_file:
        cook_book = {}
        for _line in cook_file:
            dish = _line.strip()  # Получение названия блюда
            ingredients_quant = int(cook_file.readline().strip())  # Определение количества ингредиентов блюда
            dish_dict = []
            for item in range(ingredients_quant):
                # Выбор из файла ингредиентов по разделителю '|'
                ingredient_name, quantity, unit = cook_file.readline().strip().split('|')
                #  Добавление в список словарей с ингредиентами
                dish_dict.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'unit': unit})
            cook_book[dish] = dish_dict  # Добавление в словарь блюд и их ингредиентов
            cook_file.readline()
    return cook_book


# Функция для получения списка покупок на основании заказанных блюд и количества персон
def get_shop_list_by_dishes(dishes, person_quant):
    grocery_dict = {}
    for _dish in dishes:
        # Выбор ингредиентов
        recipes = file_to_dict()
        for ingredient in recipes[_dish]:
            # Добавление ингредиетов
            if len(dishes) == 1:
                ingredient_list = dict([(ingredient['ingredient_name'],
                                         {'quantity': int(ingredient['quantity']) * person_quant,
                                          'unit': ingredient['unit']})])
            else:
                ingredient_list = dict([(ingredient['ingredient_name'],
                                     {'quantity': int(ingredient['quantity']),
                                      'unit': ingredient['unit']})])
            # Проверка наличия ингредиента в списке покупок: если есть, то увеличиваем количество,
            # иначе добавляем ингредиент в список покупок
            if ingredient['ingredient_name'] in grocery_dict:
                _plus = (int(grocery_dict[ingredient['ingredient_name']]['quantity']) +
                int(ingredient_list[ingredient['ingredient_name']]['quantity']))
                grocery_dict[ingredient['ingredient_name']]['quantity'] = str(_plus)
            else:
                grocery_dict.update(ingredient_list)
    for key, value in grocery_dict.items():
        print(key, ' : ', value)
    return grocery_dict


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос', 'Омлет', 'Запеченный картофель'], 5)
