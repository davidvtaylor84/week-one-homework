# WRITE YOUR FUNCTIONS HERE

from locale import currency
from urllib.request import parse_http_list


def get_pet_shop_name(shop_name):
    return shop_name["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

def add_or_remove_cash(total_cash, money):
    total_cash["admin"]["total_cash"] += money
    return total_cash
    
def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pets_sold, increase_in_pet_sales):
    pets_sold["admin"]["pets_sold"] += increase_in_pet_sales
    return pets_sold

def get_stock_count(stock_count):
    return len(stock_count["pets"])

def get_pets_by_breed(petshop_name, breed):
    chosen_breed = []
    for animal in petshop_name["pets"]:
        if animal["breed"] == breed:
            chosen_breed += [animal]
    return chosen_breed


def find_pet_by_name(petshop, pet_name):
    for animal in petshop["pets"]:
        if animal["name"] == pet_name:
            return animal

def remove_pet_by_name(petshop, pet_name):
    for animal in petshop["pets"]:
        if animal["name"] == pet_name:
            petshop["pets"].remove(animal)

def add_pet_to_stock(pets, new_pet):
    pets["pets"].append(new_pet) 

def get_customer_cash(customer_cash_index):
    return customer_cash_index["cash"]

def remove_customer_cash(customer, money):
    customer["cash"] -= money

def get_customer_pet_count(shopper):
    return len(shopper["pets"])

def add_pet_to_customer(shopper, new_pet):
    shopper["pets"] += [new_pet]
    
def customer_can_afford_pet(customer_cash, money):
    if customer_cash["cash"] >= money["price"]:
        return True
    else:
        return False

# def sell_pet_to_customer(pet_shop, pet, customer):
#     if customer_can_afford_pet(customer, pet) == True:
#         remove_pet_by_name(pet_shop, pet)
#         add_pet_to_customer(customer, pet)
#         get_customer_cash(customer)
#         add_or_remove_cash(pet_shop, pet["price"])

        # get_total_cash(pet_shop)
        # get_customer_cash(customer, pet["price"])
        # add_or_remove_cash(get_total_cash(pet_shop),pet["price"])
        # add_pet_to_customer(customer, pet)
        # remove_pet_by_name(pet)
        # add_or_remove_cash()

        # increase_pets_sold(get_pets_sold(pet_shop))

        # get_customer_cash(customer), pet["price"]) == True:
        # remove_pet_by_name(pet)
        # get_total_cash(add_or_remove_cash(pet_shop))
        # get_customer_cash(remove_customer_cash(customer))
        # get_pets_sold(increase_pets_sold(pet_shop))
        # add_pet_to_customer(customer)

    
    
    


# def sell_pet_to_customer(total_cash, pet_name, customer_cash):
#     total_cash[get_total_cash] += pet_name["price"]
#     customer_cash[remove_customer_cash(pet_name["price"])]
#     add_pet_to_customer(remove_pet_by_name)

    # add price of pet to total_cash - get_total_cash(cash)
    # deduct price of pet from customer - remove_customer_cash(customer, money)
    # add pet to customer - add_pet_to_customer(shopper, new_pet)
    # remove pet from pet shop - remove_pet_by_name(petshop, get_name)
    # total_cash[get_total_cash] += pet_name["price"]
    # remove_customer_cash(pet_name["price"])
    # add_pet_to_customer
    # remove_pet_by_name

    # get_customer_pet_count
    # get_pets_sold
    # get_customer_cash
    # get_total_cash
    

    # customer_cash["cash"] -= pet_name["price"]
    # total_cash["admin"]["total_cash"] += pet_name["price"]
    # shopper = []
    # for animal in pet_name["pets"]:
    #     if animal["name"] == pet_name:
    #         pet_name["pets"].remove(animal)
    #         shopper["pets"] += animal
 

    # pet_price = 0
    # if pet_name == ["name"]:
    #     pet_price += ["price"]
    # customer_cash["cash"] -= pet_price
    # total_cash["admin"]["total_cash"] += pet_price
