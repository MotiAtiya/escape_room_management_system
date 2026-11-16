from .printer import display_option_title, display_function_title
from .menu import get_action,enter_to_continue
from .rooms import search_room_by_id
from .user_input import ask
from ..validations.parsers import parse_date
import datetime


def total_active_bookings(bookings):
    if not bookings:
        raise ValueError("There are no bookings in the system")
    
    counter = 0
    for b in bookings:
        if b['status'] == "Active":
            counter += 1
    print(counter)
    

def total_inactive_bookings(bookings):
    if not bookings:
        raise ValueError("There are no bookings in the system")
    
    counter = 0
    for b in bookings:
        if b['status'] == "Cancelled":
            counter += 1
    print(counter)


def total_rvenue(bookings):
    if not bookings:
        raise ValueError("There are no bookings in the system")
    
    total = sum(b['total_price'] for b in bookings if b['status'] == "Active")
    print(total)


def total_cancellation_fees(bookings):
    if not bookings:
        raise ValueError("There are no bookings in the system")
    
    total = sum(b['cancellation_fee'] for b in bookings)
    print(total)


def get_booking_per_room(bookings, rooms = None):
    if not bookings:
        raise ValueError("There are no bookings in the system")
    
    rooms_instances = {}
    if rooms:
        for r in rooms:
            rooms_instances[r['room_id']] = 0
    for b in bookings:
        rooms_instances[b['room_id']] = rooms_instances.get(b['room_id'], 0) + 1
    return rooms_instances


def most_booked_room(bookings):
    rooms_instances = get_booking_per_room(bookings)
    most = max(rooms_instances, key=rooms_instances.get) # type: ignore
    print(f"{most} with {rooms_instances[most]} instances")
    

def bookings_per_room(rooms, bookings):
    rooms_instances = get_booking_per_room(bookings, rooms)
    print("Room ID".ljust(10), "Num of Bookings")
    print()
    for room_id, istances in rooms_instances.items():
        print(str(room_id).ljust(10), istances)


def room_occupancy_rate_in_date(rooms, bookings):
    if not bookings:
        raise ValueError("There are no bookings in the system")
    
    room = search_room_by_id(rooms)
    date = ask(parse_date, "Enter booking date [dd/mm/yyyy]: ")
    duration = datetime.timedelta(minutes = room['duration'])
    preparation_time = datetime.timedelta(minutes = 15)
    total_activity_time = datetime.timedelta(hours = 12)
    total_activity_utilization = datetime.timedelta()

    formated_date = date.strftime("%Y-%m-%d")
    for b in bookings:
        if b['status'] == "Active" and b['room_id'] == room['room_id'] and b['booking_date'] == formated_date:
            b_time = datetime.datetime.strptime(b['start_time'], "%H:%M")
            b_datetime = datetime.datetime.combine(date.date(), b_time.time())
            if b_datetime > b_datetime.replace(hour=22):
                total_activity_utilization += duration
            else:
                total_activity_utilization += duration + preparation_time

    result = round(total_activity_utilization / total_activity_time * 100, 2)
    print(result, '%')
    

def reports(rooms, bookings):

    menu = {
        1: ("Total Active Bookings", lambda: total_active_bookings(bookings)),
        2: ("Total Inactive Bookings", lambda: total_inactive_bookings(bookings)),
        3: ("Total Rvnenue", lambda: total_rvenue(bookings)),
        4: ("Total Cancellation Fees", lambda: total_cancellation_fees(bookings)),
        5: ("The most booked room", lambda: most_booked_room(bookings)),
        6: ("Number of bookings per room", lambda: bookings_per_room(rooms, bookings)),
        7: ("Room Occupancy Rate in Date", lambda: room_occupancy_rate_in_date(rooms, bookings)),
        8: ("Back to Main Menu", None)
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
