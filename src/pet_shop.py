# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(shop_name):
    return shop_name["name"]

def get_total_cash(cash):
    return cash["admin"]["total_cash"]

def add_or_remove_cash(total_cash, money):
    total_cash["admin"]["total_cash"] += money
    return total_cash
    



 