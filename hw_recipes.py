def create_all_elements_list():
    list_dish = []
    with open('recipes.txt', encoding='utf-8') as f:
        list_from_string = [line.strip() for line in f]
        list_with_slash = []
        for i in list_from_string:
            if i != '':
                list_with_slash.append(i)
            else:
                n = i.replace('', '/')
                list_with_slash.append(n)
        list_to_string = ','.join(list_with_slash)
        string_to_list = list_to_string.split(sep='/')
        list_strip = []
        for i in string_to_list:
            i = i.strip(', ')
            list_strip.append(i)
        for i in list_strip:
            list_dish.append(i.split(sep=','))
    return list_dish


def get_list_names_dishes():
    list_dishes = []
    for i in create_all_elements_list():
        list_dishes.append(i[0])
    return list_dishes


def get_dishes_ingredients():
    lst = []
    lst_sep = []
    lst_sep_stick = []
    lst_strip = []
    for i in create_all_elements_list():
        lst.append(i[2:])

    for n in lst:
        for f in n:
            lst_sep.append(f.split(sep=','))

    for k in lst_sep:
        for j in k:
            lst_sep_stick.append(j.split('|'))

    for g in lst_sep_stick:
        for s in g:
            lst_strip.append(s.strip())

    fin = [lst_strip[i:i + 3] for i in range(0, len(lst_strip), 3)]
    return fin


def get_list_count():
    count_igredients = []
    for i in create_all_elements_list():
        count_igredients.append(i[1])
    return count_igredients


def zip_ingred():
    lst_zip = []
    list_keys_ingredient = ['ingredient_name', 'quantity', 'measure']

    for i in get_dishes_ingredients():
        lst_zip.append(dict(zip(list_keys_ingredient, i)))
    return lst_zip


def final_list_ingredients():
    fin = []
    start = 0
    end = int(get_list_count()[0])
    # print(f'[{start}:{end}]')
    fin.append(zip_ingred()[start:end])
    for i in get_list_count()[1:]:
        start = end
        end += int(i)
        # print(f'[{start}:{end}]')
        fin.append(zip_ingred()[start:end])
    return fin


cook_book = dict(zip(get_list_names_dishes(), final_list_ingredients()))


def find_double_ingredients(list_ingred_double, name):
    dict_ing = {}

    for n in list_ingred_double:
        dict_ing[n] = 0

    for k in list_ingred_double:
        dict_ing[k] += 1
    return dict_ing[name]


def get_shop_list_by_dishes(dishes, person_count):
    list_ingred_double = []
    person_dishes = {}
    for i in dishes:
        for key in cook_book:
            if i == key:
                for n in cook_book[key]:
                    list_ingred_double.append(n['ingredient_name'])
                    for s in list_ingred_double:
                        double = find_double_ingredients(list_ingred_double, s)
                        person_dishes[n['ingredient_name']] = \
                            {f'measure': n['measure'], 'quantity': (int(n['quantity']) * person_count * double)}

    return person_dishes


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))


