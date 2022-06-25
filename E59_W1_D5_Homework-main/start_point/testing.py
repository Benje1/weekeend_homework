list_customers = [
{
    "name": "Alice",
    "pets": [],
    "cash": 1000
            },
{
    "name": "Bob",
    "pets": [],
    "cash": 50
},
    {
    "name": "Jack",
    "pets": [],
    "cash": 100
    }
]

new_pet = {
"name": "Bors the Younger",
"pet_type": "cat",
"breed": "Cornish Rex",
"price": 100
}

cc_pet_shop = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}


def get_pet_shop_name(pet_name):
    return pet_name["name"]

name = get_pet_shop_name(cc_pet_shop)
print(name)

# def get_pets_by_breed(pet_type, breed):
#     count = []
#     species = (pet_type["pets"])
#     for pet in species:
#         if pet ["breed"] == breed:
#             count.append(pet["name"])
#     return count

# pets = get_pets_by_breed(cc_pet_shop, "British Shorthair")
# print(pets)


# type_pet = cc_pet_shop["pets"]
# for breed in type_pet:
#     if breed == "breed":
#         print(breed)

# print(cc_pet_shop["pets"])
# all_pets = cc_pet_shop["pets"]
# print(all_pets)

def find_pet_by_name(pet_list, pet_name):
    count = []
    name = (pet_list["pets"])
    for pet in name:
        if pet ["name"] == pet_name:
            count.append(pet)
    return count
        


pet_name = find_pet_by_name(cc_pet_shop, "Arthur")
print(pet_name)


test_name = [{'name': 'Arthur', 'pet_type': 'dog', 'breed': 'Husky', 'price': 900}]

print(test_name["name"])