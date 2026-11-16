import datetime

def validate_date(date):
    cureent_date = datetime.datetime.now()
    if cureent_date > date:
        raise ValueError("Date must be in the future")
    if date > datetime.datetime(cureent_date.year + 1, cureent_date.month, cureent_date.day):
        raise ValueError("Date so far")


def get_datetime_by_date_and_time(booking_date, start_time):
    year, month, day = booking_date.split('-')
    hour, minut = start_time.split(':')
    return datetime.datetime(int(year), int(month), int(day), int(hour), int(minut))
    

def validate_room_time(new_datetime:datetime.datetime, room, bookings, skip_booking_id = None):
    start_day = new_datetime.replace(hour=10)
    end_day = new_datetime.replace(hour=22)
    
    if new_datetime < start_day:
        raise ValueError("The escape room is open from 10:00")

    duration = datetime.timedelta(minutes = room['duration'])
    preparation_time = datetime.timedelta(minutes = 15)

    if new_datetime + duration > end_day:
        raise ValueError(f"The game must finish before 22:00 (the game takes {room['duration']} minutes)")

    new_end = new_datetime + duration + preparation_time

    for b in bookings:
        if skip_booking_id and b['booking_id'] == skip_booking_id:
            continue

        if b['room_id'] == room['room_id']:
            existing_start = get_datetime_by_date_and_time(b['booking_date'], b['start_time'])
            if existing_start.date() == new_datetime.date():
                existing_end = existing_start + duration + preparation_time
                if new_datetime < existing_end and new_end > existing_start:
                    raise ValueError("There is another booking at this time")
