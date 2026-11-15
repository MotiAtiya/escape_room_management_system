from func.storage import load_rooms, load_bookings
from func.rooms import rooms_management
from func.bookings import bookings_management
from func.reports import reports
from func.printer import display_system_title
from func.menu import get_action


def main():
    rooms = load_rooms()
    bookings = load_bookings()

    print(rooms)
    print(bookings)

    menu = {
        1: ("Rooms Management", lambda: rooms_management(rooms)),
        2: ("Bookings Management", lambda: bookings_management(rooms, bookings)),
        3: ("Reports", lambda: reports(rooms, bookings)),
        4: ("Exit", None)
    }

    while True:
        display_system_title()
        _, action = get_action(menu)
        if action is None:
            print("Bye!")
            break

        action()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
