from .printer import display_option_title, display_function_title, display_bookings, display_booking_details
from .menu import get_action, enter_to_continue
from .rooms import search_room_by_id, get_room_by_id
from .user_input import ask, edit
from ..validations.date_time_validators import validate_date, validate_room_time
from ..validations.parsers import parse_from_range, parse_date, parse_time, parse_string, parse_booking_id, parse_room_id, parse_yes_no_confirmation
from .storage import dump_bookings
import datetime


def get_next_booking_id(bookings):
    latest = max(bookings, key=lambda b: b['booking_id'][1:])
    latest_id = int(latest["booking_id"][1:])
    return 'B' + str(latest_id + 1).zfill(3)


def calculate_price(base_price, num_of_players, day):
    price = base_price * num_of_players
    if 5 <= num_of_players <= 6:
        price -= price * 10 / 100
    elif num_of_players >= 7:
        price -= price * 15 / 100

    # Friday is 4, Saturday is 5
    if day in [4,5]: 
        price += price * 15 / 100
    
    return round(price, 2)


def add_booking(rooms, bookings):
    customer_name = ask(parse_string, "Enter customer name: ")
    room = search_room_by_id(rooms)
    if not room['is_active']:
        raise ValueError("This room is inactive")

    date = ask(parse_date, "Enter booking date [dd/mm/yyyy]: ")
    validate_date(date)

    while True:
        try:
            time = ask(parse_time, "Enter booking time [hh:mm]: ")
            booking_datetime = datetime.datetime.combine(date, time)
            validate_room_time(booking_datetime, room, bookings)
            break
        except ValueError as e:
            print("Error:", e)

    num_of_players = ask(parse_from_range(room['min_players'], room['max_players']), "Enter num of players: ")

    new_booking = {
        "booking_id": get_next_booking_id(bookings),
        "customer_name": customer_name,
        "room_id": room['room_id'],
        "booking_date": booking_datetime.strftime("%Y-%m-%d"),
        "start_time": booking_datetime.strftime("%H:%M"),
        "players": num_of_players,
        "total_price": calculate_price(room['price_per_player'], num_of_players, booking_datetime.weekday()),
        "status": "Active",
        "cancellation_fee": 0.0
    }
    bookings.append(new_booking)
    dump_bookings(bookings)
    print(f"\nbooking {new_booking['booking_id']} added successfuly!")
    

def search_booking_by_id(bookings):
    if not bookings:
        raise ValueError("There are no bookings in the system")
    
    booking_id = ask(parse_booking_id, "Enter booking ID: ")
    for b in bookings:
        if b['booking_id'] == booking_id:
            return b
    raise ValueError("Booking not found")


def booking_details(bookings):
    booking = search_booking_by_id(bookings)
    display_booking_details(booking)


def search_bookings_by_customer_name(bookings):
    if not bookings:
        raise ValueError("There are no bookings in the system")
    
    customer_name = ask(parse_string, "Enter customer name: ")
    result = []
    for b in bookings:
        if b['customer_name'].lower() == customer_name.lower():
            result.append(b)
    if not result:
        raise ValueError("This customer name has not bookings")
    return result


def customer_bookings(bookings):
    booking_list = search_bookings_by_customer_name(bookings)
    display_bookings(booking_list)


def search_bookings_by_date(bookings):
    if not bookings:
        raise ValueError("There are no bookings in the system")
    
    date = ask(parse_date, "Enter booking date [dd/mm/yyyy]: ")
    formated_date = date.strftime("%Y-%m-%d")
    result = []
    for b in bookings:
        if b['booking_date'] == formated_date:
            result.append(b)
    if not result:
        raise ValueError("There are not bookings in this date")
    return result


def bookings_in_date(bookings):
    booking_list = search_bookings_by_date(bookings)
    display_bookings(booking_list)


def update_booking(rooms, bookings):
    booking = search_booking_by_id(bookings)

    customer_name = edit(parse_string, "Enter customer name", booking['customer_name'])
    room = get_room_by_id(rooms, edit(parse_room_id, "Enter room ID: ", booking['room_id']))
    if not room['is_active']:
        raise ValueError("This room is inactive")

    year, month, day = booking['booking_date'].split('-')
    date = datetime.datetime(int(year), int(month), int(day))
    date = edit(parse_date, "Enter booking date [dd/mm/yyyy]", date)
    validate_date(date)

    while True:
        try:
            hour, minute = booking['start_time'].split(':')
            time = datetime.time(int(hour), int(minute))
            time = edit(parse_time, "Enter booking time [hh:mm]", time)
            booking_datetime = datetime.datetime.combine(date, time)
            validate_room_time(booking_datetime, room, bookings, booking['booking_id'])
            break
        except ValueError as e:
            print("Error:", e)

    num_of_players = edit(parse_from_range(room['min_players'], room['max_players']), "Enter num of players: ", booking['players'])

    booking['customer_name'] = customer_name
    booking['room_id'] = room['room_id']
    booking['booking_date'] = booking_datetime.strftime("%Y-%m-%d")
    booking['start_time'] = booking_datetime.strftime("%H:%M")
    booking['players'] = num_of_players
    booking['total_price'] = calculate_price(room['price_per_player'], num_of_players, booking_datetime.weekday())

    dump_bookings(bookings)
    print(f"\nbooking {booking['booking_id']} updated successfuly!")


def calculate_cancellation_fee(booking_datetime, current_datetime, price):
    if current_datetime + datetime.timedelta(hours=24) < booking_datetime:
        return 0
    
    if current_datetime + datetime.timedelta(hours=6) <= booking_datetime <= current_datetime + datetime.timedelta(hours=24):
        return price * 25 / 100
    
    if booking_datetime < current_datetime + datetime.timedelta(hours=6):
        return price * 50 / 100
    

def cancel_booking(bookings):
    booking = search_booking_by_id(bookings)
    if booking['status'] == "Cancelled":
        raise ValueError("This booking already cancelled before")
    
    booking_date = datetime.datetime.strptime(booking['booking_date'], "%Y-%m-%d")
    booking_time = datetime.datetime.strptime(booking['start_time'], "%H:%M")
    booking_datetime = datetime.datetime.combine(booking_date.date(), booking_time.time())
    current_datetime = datetime.datetime.now()

    if booking_datetime < current_datetime:
        raise ValueError("The order has already been redeemed. It cannot be cancelled")
    
    fee = calculate_cancellation_fee(booking_datetime, current_datetime, booking['total_price'])

    user_confirm = ask(parse_yes_no_confirmation, f"Are you sure to cancel the booking? It will cost you a fee of {fee} [y/n]: ")
    if user_confirm == 'y':
        booking['status'] = "Cancelled"
        booking['cancellation_fee'] = fee
        dump_bookings(bookings)
        print(f"\nBooking {booking['booking_id']} cancelled successfuly!")
    else:
        print(f"\nCancel cancelled!")


def bookings_management(rooms, bookings):
    menu = {
        1: ("Create New Booking", lambda: add_booking(rooms, bookings)),
        2: ("Display All Bookings", lambda: display_bookings(bookings)),
        3: ("Search Booking", lambda: booking_details(bookings)),
        4: ("Display Customer Bookings", lambda: customer_bookings(bookings)),
        5: ("Display Bookings in Date", lambda: bookings_in_date(bookings)),
        6: ("Change Booking Details", lambda: update_booking(rooms, bookings)),
        7: ("Cancel Booking", lambda: cancel_booking(bookings)),
        8: ("Back to Main Menu", None)
    }

    while True:
        display_option_title("Products Management")
        title, action = get_action(menu)
        if action is None:
            break

        try:
            display_function_title(title)
            action()
        except ValueError as e:
            print("Error:", e)
        finally:
            enter_to_continue()
