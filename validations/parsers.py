import re
import datetime

def parse_string(raw):
    string = raw.strip()
    if not string:
        raise ValueError("Cannot be empty")
    return " ".join(string.split()).title()


def parse_id(raw, prefix):
    room_id = parse_string(raw)
    if room_id[:1] in prefix:
        room_id = room_id[1:]
    elif room_id[:1].isalpha():
        raise ValueError(f"ID must be of the form '{prefix[0]}x' when x is integer. For example: {prefix[0]}001")
    room_id = parse_positive_int_number(room_id)
    return str(room_id).zfill(3)


def parse_room_id(raw):
    return 'R' + parse_id(raw, ['R', 'r'])


def parse_booking_id(raw):
    return 'B' + parse_id(raw, ['B', 'b'])


def parse_positive_int_number(raw):
    int_num = raw.strip()
    if not int_num:
        raise ValueError("Cannot be empty")
    try:
        int_num = int(int_num)
    except ValueError:
        raise ValueError("Must be an integer number")
    if int_num <= 0:
        raise ValueError("Must be a positive number")
    return int_num
    

def parse_float_number(raw):
    float_num = raw.strip()
    if not float_num:
        raise ValueError("Cannot be empty")
    try:
        float_num = float(float_num)
    except ValueError:
        raise ValueError("Must be a number")
    return float_num


def parse_positive_float_number(raw):
    pos_float_num = parse_float_number(raw)
    if pos_float_num <= 0:
        raise ValueError("Must be a positive number")
    return pos_float_num


def parse_not_negative_int_number(raw):
    stock = raw.strip()
    if not stock:
        raise ValueError("Cannot be empty")
    try:
        stock = int(stock)
    except ValueError:
        raise ValueError("Must be an integer number")
    if stock < 0:
        raise ValueError("Must be a not negative number")
    return stock


def parse_from_range(minimum, maximum):
    def parser(raw):
        value = raw.strip()
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Must be an integer number")
        else:
            if not minimum <= value <= maximum:
                raise ValueError(f"Invalid value. Enter from {minimum} to {maximum}")
            return value
    return parser


def parse_yes_no_confirmation(raw):
    confirm = raw.strip()
    if not confirm:
        raise ValueError("Cannot be empty")
    if confirm not in ['yes', 'y', 'Y', 'no', 'n', 'N']:
        raise ValueError("Invalid input. Only yes (y) or no (n)")
    return 'y' if confirm in ['yes', 'y', 'Y'] else 'n'


def parse_percentage(raw):
    percentage = parse_float_number(raw)
    if not 0 <= percentage <= 100:
        raise ValueError("Must be between 0-100")
    return percentage


def parse_date(raw):
    raw_date = parse_string(raw)
    day, month, year = re.split(r"[.,\-/:\s]+", raw_date)
    date = datetime.datetime(int(year), int(month), int(day))
    return date


def parse_time(raw):
    raw_time = parse_string(raw)
    hour, minute = re.split(r"[.,\-/:\s]+", raw_time)
    time = datetime.time(int(hour), int(minute))
    return time

