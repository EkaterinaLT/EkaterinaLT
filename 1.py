def cook_book_from_file():
    cook_book = {}
    with open('1.txt') as dishes_list:
     for line in dishes_list:
       dish_name = line.strip()
       if line in ['\n']:
        continue
       else:
        cook_book[dish_name] = []
        ingridients_quantity = int(dishes_list.readline().strip())
        for _ in range(ingridients_quantity):
         ingridient = dishes_list.readline().split(' | ')
         cook_book_info  = {
        'ingridient_name' : ingridient[0],
        'quantity':   ingridient[1],
         'measure' :ingridient[2]
         }
         cook_book[dish_name].append(cook_book_info)
     return cook_book


def get_shop_list_by_dishes(dishes, person_count,cook_book):
 shop_list = {}
 for dish in dishes:
  for ingridient in cook_book[dish]:
   new_shop_list_item = dict(ingridient)
   new_shop_list_item['quantity'] *= person_count
   if new_shop_list_item['ingridient_name'] not in shop_list:
    shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
   else:
    shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
 return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').split(', ')
    print('Рецепт из файла: ')
    cook_book = cook_book_from_file()
    shop_list = get_shop_list_by_dishes(dishes, person_count,cook_book)
    print_shop_list(shop_list)


create_shop_list()
