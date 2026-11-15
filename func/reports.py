from .printer import display_option_title, display_function_title
from .menu import get_action,enter_to_continue

def total_active_bookings(bookings):
    pass

def total_inactive_bookings(bookings):
    pass

def total_rvenue(bookings):
    pass

def total_cancellation_fees(bookings):
    pass

def most_booked_room(bookings):
    pass

def bookings_per_room(rooms, bookings):
    pass

def room_occupancy_rate_in_date(rooms, bookings):
    pass


def reports(rooms, bookings):

    menu = {
        "1": ("Total Active Bookings", lambda: total_active_bookings(bookings)),
        "2": ("Total Inactive Bookings", lambda: total_inactive_bookings(bookings)),
        "3": ("Total Rvnenue", lambda: total_rvenue(bookings)),
        "4": ("Total Cancellation Fees", lambda: total_cancellation_fees(bookings)),
        "5": ("The most booked room", lambda: most_booked_room(bookings)),
        "6": ("Number of bookings per room", lambda: bookings_per_room(rooms, bookings)),
        "7": ("Room Occupancy Rate in Date", lambda: room_occupancy_rate_in_date(rooms, bookings)),
        "8": ("Back to Main Menu", None)
    }

    while True:
        display_option_title("Reports")
        title, action = get_action(menu)
        if action is None:
            break

        try:
            display_function_title(title)
            action()
        except ValueError as e:
            print("Error:", e)
        finally: enter_to_continue()
