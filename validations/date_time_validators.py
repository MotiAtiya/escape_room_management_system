import datetime

from func.consts import ROOM_OPENING_TIME, ROOM_CLOSING_TIME, ROOM_PREPERATION_TIME


def validate_date(date):
    cureent_date = datetime.datetime.now()
    if cureent_date > date:
        raise ValueError("Date must be in the future")
    if date > cureent_date.replace(year = cureent_date.year+1):
        raise ValueError("Date so far")


def validate_room_time(new_start:datetime.datetime, room, bookings, skip_booking_id = None):
    start_day = new_start.replace(hour=ROOM_OPENING_TIME)
    end_day = new_start.replace(hour=ROOM_CLOSING_TIME)
    
    if new_start < start_day:
        raise ValueError(f"The escape room is open from {ROOM_OPENING_TIME}:00")

    duration = datetime.timedelta(minutes = room['duration'])
    preparation_time = datetime.timedelta(minutes = ROOM_PREPERATION_TIME)

    if new_start + duration > end_day:
        raise ValueError(f"The game must finish before {ROOM_CLOSING_TIME}:00 (the game takes {room['duration']} minutes)")

    new_end = new_start + duration + preparation_time

    for b in bookings:
        if skip_booking_id and b['booking_id'] == skip_booking_id:
            continue

        if b['room_id'] == room['room_id']:
            existing_start = datetime.datetime.strptime(b['booking_date'] + b['start_time'], "%Y-%m-%d %H:%M")
            if existing_start.date() == new_start.date():
                existing_end = existing_start + duration + preparation_time
                if new_start < existing_end and new_end > existing_start:
                    raise ValueError("There is another booking at this time")
