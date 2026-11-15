def parse_string(raw):
    string = raw.strip()
    if not string:
        raise ValueError("Cannot be empty")
    return " ".join(string.split()).title()


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


def choice_from(options):
    def parser(raw):
        choice = raw.strip()
        try:
            int(choice)
        except ValueError:
            raise ValueError("Must be an integer number")
        else:
            if choice not in options:
                raise ValueError("Invalid choice")
            return choice
    return parser


def parse_yes_no_confirmation(raw):
    confirm = raw.strip()
    if not confirm:
        raise ValueError("Cannot be empty")
    if confirm not in ['yes', 'y', 'Y', 'no', 'n', 'N']:
        raise ValueError("Invalid choise. Only yes (y) or no (n)")
    return 'y' if confirm in ['yes', 'y', 'Y'] else 'n'


def parse_percentage(raw):
    percentage = parse_float_number(raw)
    if not 0 <= percentage <= 100:
        raise ValueError("Must be between 0-100")
    return percentage
    