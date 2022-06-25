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
#     count = {}
#     name = (pet_list["pets"])
#     for pet in name:
#         if pet ["name"] == pet_name:
#             count = pet
#             return count
#         else:
#             count = None
#             return

def find_pet_by_name(pet_list, pet_name):
    count = None
    name = (pet_list["pets"])
    for pet in name:
        if pet ["name"] == pet_name:
            count = pet
    return count

# def remove_pet_by_name(shop, pet_to_remove):
#     # shop["pets"]["name"].pop(pet_to_remove)
#     for pet in shop["pets"]:
#         if pet["name"] == pet_to_remove:
#             shop["pet"].remove(pet_to_remove)

def remove_pet_by_name(shop, pet_to_remove):
    for pet in shop["pets"]:
        if pet["name"] == pet_to_remove:
            shop["pets"].remove(pet)


def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet.copy())

def get_customer_cash(customer):
    money = 0
    money += customer["cash"]
    return money

def remove_customer_cash(customer, fee):
    customer["cash"] -= fee


# for godsake remember that you are useing a list!!!!!!!
def get_customer_pet_count(customer):
    pet_count = []
    for pet in customer["pets"]:
        pet_count.appened(pet)
    return len(pet_count)

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet.copy())