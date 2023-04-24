# task_1.4.py()
titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}


store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

for name_product, code_product in titles.items():
    total_quantity = 0
    total_price = 0
    for sports_equipment in store[code_product]:
        all_quantity = 0
        all_price = 0
        all_quantity += sports_equipment['quantity']
        all_price += sports_equipment['price']
        total_price += all_quantity * all_price
        total_quantity += all_quantity
    print('{0} - {1} шт, стоимость  {2} руб'.format(name_product, total_quantity, total_price))
