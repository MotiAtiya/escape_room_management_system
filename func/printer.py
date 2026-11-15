from .helpers import clear_screen


# def display_single_product(product:dict):
#     print("Product ID:", product['id'])
#     print("Name:", product['name'])
#     print("Category:", product['category'])
#     print("Price:", product['price'])


# def display_products(products:list):
#     print("ID".ljust(5), "Name".ljust(40), "Category".ljust(30), "Price".ljust(10), "Stock".ljust(10))
#     print()
#     for p in products:
#         print(str(p['id']).ljust(5), str(p['name']).ljust(40), str(p['category']).ljust(30), str(p['price']).ljust(10), p['stock'])


# def display_active_products(products:list):
#     display_products(list(filter(lambda p: p['active'] ,products)))


def display_rooms(rooms):
    # if not rooms:
    #     raise

    print("ID".ljust(10), "Name".ljust(20), "difficulty".ljust(15), "Duration".ljust(10), "Players".ljust(10), "Price".ljust(10), "Is active".ljust(10))
    print()
    for r in rooms:
        print(str(r['room_id']).ljust(10), str(r['name']).ljust(20), str(r['difficulty']).ljust(15), str(r['duration']).ljust(10), f"{r['min_players']} - {r['max_players']}".ljust(10), str(r['price_per_player']).ljust(10), "True" if r['is_active'] else "False")


def display_room_details(room):
    print("Room ID:".ljust(20), room['room_id'])
    print("Name:".ljust(20), room['name'])
    print("Difficulty:".ljust(20), room['difficulty'])
    print("Duration:".ljust(20), room['duration'], "min")
    print("Min Players:".ljust(20), room['min_players'])
    print("Max Players:".ljust(20), room['max_players'])
    print("Price Per Player:".ljust(20), room['price_per_player'])
    print("Is Active:".ljust(20), "True" if room['is_active'] else "False")


def display_bookings(bookings):
    pass
    
def display_menu(menu):
    for index, option in menu.items():
        print(f"{index}. {option[0]}")


def display_system_title():
    clear_screen()
    print("""
===========================================
       ESCAPE ROOM MANAGEMENT SYSTEM
===========================================
    """)


def display_option_title(option_title):
    clear_screen()
    print(f"\n--------- {option_title.upper()} ---------\n")


def display_function_title(function_title):
    clear_screen()
    print(function_title)
    print("-" * len(function_title))
    print()

# def display_sale_summary(sale):
#     for item in sale['items']:
#         print(f"{str(item['name']).ljust(25)}{item['quantity']} X {item['unit_price']} = {item['total']}")

#     print("\n------------------------------------")
#     print(f"{('Subtotal:').ljust(30)}{sale['subtotal']}")
#     print(f"{('Discount:').ljust(30)}{sale['discount']}%")
#     print(f"{('Total:').ljust(30)}{sale['total']}")
#     print("====================================")

