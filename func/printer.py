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
    pass


def display_room_details(room):
    pass


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

