from .printer import display_option_title, display_function_title, display_rooms, display_room_details
from .menu import get_action, enter_to_continue
from .user_input import ask, edit
from .validators import parse_room_id, parse_string, parse_from_range, parse_positive_int_number, parse_yes_no_confirmation
from .storage import dump_rooms

def get_room_by_id(rooms, room_id):
    for r in rooms:
        if r['room_id'] == room_id:
            return r
    raise ValueError("Room not found")


def search_room_by_id(rooms):
    room_id = ask(parse_room_id, "Enter room ID: ")
    return get_room_by_id(rooms, room_id)


def room_details(rooms):
    room = search_room_by_id(rooms)
    display_room_details(room)


def get_next_room_id(rooms):
    latest = max(rooms, key=lambda r: r['room_id'][1:])
    latest_id = int(latest["room_id"][1:])
    return 'R' + str(latest_id + 1).zfill(3)


def get_difficulty_description(val):
    difficulty = {
        1: "Easy",
        2: "Medium",
        3: "Hard"
    }
    if val in difficulty.values():
        return val
    return difficulty[val]


def add_room(rooms):
    name = ask(parse_string, "Enter room Name: ")
    difficulty = ask(parse_from_range(1, 3), "Enter difficulty [1: Easey, 2: Medium, 3: Hard]: ")
    duration = ask(parse_from_range(30, 120), "Enter game duration [from 30 min to 120 min]: ")
    min_players = ask(parse_from_range(1, 10), "Enter minimum number of players [1-10]: ")
    max_players = ask(parse_from_range(min_players, 40), f"Enter maximum number of players [{min_players}-40]: ")
    price_per_player = ask(parse_positive_int_number, "Enter price per player: ")

    new_room = {
        "room_id": get_next_room_id(rooms),
        "name": name,
        "difficulty": get_difficulty_description(difficulty),
        "duration": duration,
        "min_players": min_players,
        "max_players": max_players,
        "price_per_player": price_per_player,
        "is_active": True
    }
    rooms.append(new_room)
    dump_rooms(rooms)
    print(f"\nroom {name} added successfuly!")


def update_room(rooms):
    room = search_room_by_id(rooms)

    name = edit(parse_string, "Enter room Name", room['name'])
    difficulty = get_difficulty_description(edit(parse_from_range(1, 3), "Enter difficulty [1: Easey, 2: Medium, 3: Hard]", room['difficulty']))
    duration = edit(parse_from_range(30, 120), "Enter game duration [from 30 min to 120 min]", room['duration'])
    min_players = edit(parse_from_range(1, 10), "Enter minimum number of players [1-10]", room['min_players'])
    max_players = edit(parse_from_range(min_players, 40), f"Enter maximum number of players [{min_players}-40]", room['max_players'])
    price_per_player = edit(parse_positive_int_number, "Enter price per player", room['price_per_player'])

    room['name'], room['difficulty'], room['duration'], room['min_players'], room['max_players'], room['price_per_player'] = \
        name, difficulty, duration, min_players, max_players, price_per_player
    
    dump_rooms(rooms)
    print(f"\nroom {room['name']} updated successfuly!")


def active_or_inactive_room(rooms):
    room = search_room_by_id(rooms)
    status = room['is_active']

    if status:
        msg = "The room is active now. Are you sure you want to inactive it? [y/n]: "
    else:
        msg = "The room is inactive now. Are you sure you want to active it? [y/n]: "
    
    user_confirm = ask(parse_yes_no_confirmation, msg)
    if user_confirm == 'y':
        room['is_active'] = not room['is_active']
        dump_rooms(rooms)
        print(f"\nroom {room['name']} updated successfuly!")
    else:
        print(f"\nUpdating cancelled!")


def rooms_management(rooms):
    menu = {
        1: ("Display All Rooms", display_rooms),
        2: ("Display Room Details", room_details),
        3: ("Add Room", add_room),
        4: ("Update Room", update_room),
        5: ("Active or Inactive Room", active_or_inactive_room),
        6: ("Back to Main Menu", None)
    }

    while True:
        display_option_title("Products Management")
        title, action = get_action(menu)
        if action is None:
            break

        try:
            display_function_title(title)
            action(rooms)
        except ValueError as e:
            print("Error:", e)
        finally:
            enter_to_continue()
