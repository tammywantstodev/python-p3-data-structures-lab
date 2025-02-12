spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_food=[]
    for foods in spicy_foods:
        food_name=foods.get('name')
        spicy_food.append(food_name)
    return spicy_food

def get_spiciest_foods(spicy_foods):
    spiciest_foods=[]
    for foods in spicy_foods:
        spice_level=foods.get("heat_level")
        if spice_level>5:
            spiciest_foods.append(foods)
    return spiciest_foods


def print_spicy_foods(spicy_foods):
    for foods in spicy_foods:
        name=foods.get("name")
        cuisine=foods.get("cuisine")
        heat_level=foods.get("heat_level")
        chillies="🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {chillies}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
       for food in spicy_foods:  
        if food["cuisine"] == cuisine:  
            return food


def print_spiciest_foods(spicy_foods):
    for foods in spicy_foods:
        name=foods.get("name")
        cuisine=foods.get("cuisine")
        heat_level=foods.get("heat_level")
        chillies="🌶" * heat_level
        if heat_level>5:
            print(f"{name} ({cuisine}) | Heat Level: {chillies}")

def get_average_heat_level(spicy_foods):
    sum_of_heat=[]
    for foods in spicy_foods:
        heat_level=foods.get("heat_level")
        sum_of_heat.append(heat_level)
    return int(sum(sum_of_heat)/ len(sum_of_heat))

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

