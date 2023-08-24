products = {
    1: {
        "id": 1,
        "name": "Computer",
        "price": 1000,
        "id_cat": 1
    },
    2: {
        "id": 2,
        "name": "Mouse",
        "price": 10,
        "id_cat": 2
    },
    3: {
        "id": 3,
        "name": "Keyboard",
        "price": 20,
        "id_cat": 2
    },
    4: {
        "id": 4,
        "name": "Monitor",
        "price": 200,
        "id_cat": 1
    },
}

categories = {
    1: {
        "id": 1,
        "name": "Technology",
    },
    2: {
        "id": 2,
        "name": "Accessories",
    }
}


def get_products_and_categories():
    products_and_categories = {}
    for product_id, product in products.items():
        for category_id, category in categories.items():
            if product["id_cat"] == category["id"]:
                products_and_categories[product_id] = {
                    "id": product["id"],
                    "name": product["name"],
                    "category": category["name"]
                }
    return products_and_categories



print(get_products_and_categories())
