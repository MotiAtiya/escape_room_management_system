from .helpers import clear_screen

def display_rooms(rooms):
    # if not rooms:
    #     raise

    print("ID".ljust(10), "Name".ljust(20), "Difficulty".ljust(15), "Duration".ljust(10), "Players".ljust(10), "Price".ljust(10), "Status".ljust(10))
    print()
    for r in rooms:
        print(str(r['room_id']).ljust(10), str(r['name']).ljust(20), str(r['difficulty']).ljust(15), str(r['duration']).ljust(10), f"{r['min_players']} - {r['max_players']}".ljust(10), str(r['price_per_player']).ljust(10), "Active" if r['is_active'] else "Inactive")


def display_room_details(room):
    print()
    print("Room ID:".ljust(20), room['room_id'])
    print("Name:".ljust(20), room['name'])
    print("Difficulty:".ljust(20), room['difficulty'])
    print("Duration:".ljust(20), room['duration'], "min")
    print("Min Players:".ljust(20), room['min_players'])
    print("Max Players:".ljust(20), room['max_players'])
    print("Price Per Player:".ljust(20), room['price_per_player'])
    print("Is Active:".ljust(20), "True" if room['is_active'] else "False")


def display_bookings(bookings):
    print("ID".ljust(5), "Customer Name".ljust(20), "Room ID".ljust(8), "Date".ljust(11), "Time".ljust(7), "Players".ljust(8), "Price".ljust(8), "Status".ljust(10), "Fee")
    print()
    for b in bookings:
        print(str(b['booking_id']).ljust(5), str(b['customer_name']).ljust(20), str(b['room_id']).ljust(8), str(b['booking_date']).ljust(11), str(b['start_time']).ljust(7), str(b['players']).ljust(8), str(b['total_price']).ljust(8), str(b['status']).ljust(10), str(b['cancellation_fee']))


def display_booking_details(booking):
    print()
    print("Booking ID:".ljust(20), booking['booking_id'])
    print("Customer Name:".ljust(20), booking['customer_name'])
    print("Room ID:".ljust(20), booking['room_id'])
    print("Date:".ljust(20), booking['booking_date'])
    print("Start Time:".ljust(20), booking['start_time'])
    print("Players:".ljust(20), booking['players'])
    print("Total Price:".ljust(20), booking['total_price'])
    print("Status:".ljust(20), booking['status'])
    print("Cancellation Fee:".ljust(20), booking['cancellation_fee'])


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

