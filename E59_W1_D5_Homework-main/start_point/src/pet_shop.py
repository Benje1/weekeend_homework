def get_pet_shop_name(pet_name):
    return pet_name["name"]

def get_total_cash(admin_cash):
    return admin_cash["admin"]["total_cash"]
    
def add_or_remove_cash(admin_cash, money):
    admin_cash["admin"]["total_cash"] += money
    
def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]
    
def increase_pets_sold(more_pets, sold):
    more_pets["admin"]["pets_sold"] += sold

def get_stock_count(pet_stock):
    return len(pet_stock["pets"])


# #issues
# def get_pets_by_breed(species, breed):
#     count = []
#     for pet in species:
#         if pet == breed:
#             count.append(pet["name"])
#     return count

# def find_pet_by_name(pet, name):
#     for pet_name in pet["pets"]["name"]:
#         if pet_name == name:
#             return pet_name

# something about this is wierd, we can sue this in our own but not here
# def get_pets_by_breed(pets, breed):
#     count = []
#     for pet in pets["pets"]["breed"]:
#         if pet == breed:
#             count.append(pet["name"])
#     return count

def get_pets_by_breed(pet_type, breed):
    count = []
    species = (pet_type["pets"])
    for pet in species:
        if pet ["breed"] == breed:
            count.append(pet["name"])
    return count

# def find_pet_by_name(pet_list, pet_name):
#     count = []
#     name = (pet_list["pets"])
#     for pet in name:
#         if pet ["name"] == pet_name:
#             count.append(pet["name"])
#     return count

def find_pet_by_name(pet_list, pet_name):
    count = []
    name = (pet_list["pets"])
    for pet in name:
        if pet ["name"] == pet_name:
            count.append(pet)
    return count
