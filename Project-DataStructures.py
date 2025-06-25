# Create the Inventory
inventory = {
    "apple": (10, 2.5),
    "banana": (20, 1.2)
}

# Display the inventory
def display_inventory():
    print("\nCurrent inventory:")
    for item, (quantity, price) in inventory.items():
        print(f"Item: {item}, Quantity: {quantity}, Price: ${price}")
    print()

# Calculate total inventory value
def calculate_total_value():
    total = 0
    for quantity, price in inventory.values():
        total += quantity * price
    print(f"Total value of inventory: ${total:.2f}")

#  Add, Remove, and Update Items
def add_item(item_name, quantity, price):
    if item_name in inventory:
        print(f"{item_name} already exists. Use update_item to modify it.")
    else:
        inventory[item_name] = (quantity, price)
        print(f"Added {item_name} to inventory.")

def remove_item(item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(f"Removed {item_name} from inventory.")
    else:
        print(f"{item_name} not found in inventory.")

def update_item(item_name, new_quantity=None, new_price=None):
    if item_name in inventory:
        quantity, price = inventory[item_name]
        quantity = new_quantity if new_quantity is not None else quantity
        price = new_price if new_price is not None else price
        inventory[item_name] = (quantity, price)
        print(f"Updated {item_name}.")
    else:
        print(f"{item_name} not found in inventory.")


