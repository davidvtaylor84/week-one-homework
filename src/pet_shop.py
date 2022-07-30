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


