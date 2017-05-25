import json


def open_json_data_file(path):
    print('Читаем данные из файла: {}'.format(path))
    try:
        with open(path, 'r', encoding='utf8') as f:
            try:
                data = json.loads(f.read())
                return data
            except:
                print('Данных в файле не обнаружено.')
                return
    except:
        print('Файл данных не обнаружен.'.format(path))


def get_shop_list_by_dishes(dishes, people_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in dish['ingridients']:
            new_shop_item = dict(ingridient)
            new_shop_item['quantity'] = new_shop_item['quantity'] * people_count
            if new_shop_item['product'] not in shop_list:
                shop_list[new_shop_item['product']] = new_shop_item
            else:
                shop_list[new_shop_item['product']]['quantity'] += new_shop_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for key, shop_list_item in shop_list.items():
        print("{product} {quantity} {unit}".format(**shop_list_item))


def create_shop_list(data, people_count, first_dish, second_dish, third_dish):
    dish1 = data[first_dish]
    dish2 = data[second_dish]
    dish3 = data[third_dish]
    dishes = [dish1, dish2, dish3]
    shop_list = get_shop_list_by_dishes(dishes, people_count)
    print_shop_list(shop_list)

path = 'Задание 2-2.json'
data = open_json_data_file(path)

print('Выберите первое блюдо: ')
first_dish = input()
print('Выберите второе блюдо: ')
second_dish = input()
print('Выберите третье блюдо: ')
third_dish = input()
print('На сколько человек?')
people_count = int(input())

print('\nСписок покупок: ')
create_shop_list(data, people_count, first_dish, second_dish, third_dish)
