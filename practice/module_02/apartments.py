from collections.abc import Iterable

apartments = [
    {
        "district": "Majorna",
        "living_area": 68,
        "price": 3350000
    },
    {
        "district": "Vasastan",
        "living_area": 45,
        "price": 2900000
    },
    {
        "district": "Linnéstaden",
        "living_area": 82,
        "price": 4200000
    }
]

def calculate_average(apartments):
    total_price = 0

    for apartment in apartments:
        total_price += apartment["price"]

    return total_price / len(apartments)


average_price = calculate_average(apartments)

print("Genomsnittspris:", average_price)


for apartment in apartments:
    if apartment["price"] > average_price:
        print(apartment["district"], "är dyrare än genomsnittet")
    else:
        print(apartment["district"], "är billigare än genomsnittet")