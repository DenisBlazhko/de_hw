purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases):
    total = 0
    for item in purchases:
        total += item['price'] * item['quantity']
    return f'Общая выручка: {total}'


def items_by_category(purchases):
    total = {}
    for item in purchases:
        total[item['category']] = []
    for item in purchases:
        if item['item'] not in total[item['category']]:
            total[item['category']].append(item['item'])
    return f'Товары по категориям: {total}'


def expensive_purchases(purchases, min_price):
    total = []
    for item in purchases:
        if item['price'] >= min_price:
            total.append(item) 
    return f'Покупки дороже {min_price}: {total}'


def average_price_by_category(purchases):
    total ={}
    for item in purchases:
        total[item['category']] = []
    for category, avg in total.items():
        count = 0
        sum_price = 0
        for item in purchases:
            if category == item['category']:
                count += 1
                sum_price += item['price']
        total[category] = sum_price / count
    return f'Средняя цена по категориям: {total}'


def most_frequent_category(purchases):
    max_quantity = 0
    category_res = ''
    for item in purchases:
        if item['quantity'] >= max_quantity:
            max_quantity = item['quantity']
            category_res = item['category'] 
    return f'Категория с наибольшим количеством проданных товаров: {category_res}'


print(total_revenue(purchases))
print(items_by_category(purchases))
print(expensive_purchases(purchases, 1.0))
print(average_price_by_category(purchases))
print(most_frequent_category(purchases))