def ask(parse_input, prompt_input):
    while True:
        try:
            return parse_input(input(prompt_input))
        except ValueError as e:
            print("Error:", e)


def edit(parse_input, prompt_input, current_value):
    while True:
        try:
            user_input = input(f"{prompt_input} [{current_value}] (press Enter to keep): ")
            if not user_input:
                return current_value
            return parse_input(user_input)
        except ValueError as e:
            print("Error:", e)


