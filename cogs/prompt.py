


def text(message):
    user_input = input(message)
    if isinstance(user_input,str)
        return user_input

def number(message):
    user_input = input(message)
    if isinstance(user_input,int):
        return user_input
    else:
        try:
            user_input = int(user_input)
            return user_input
        except Exception as e:
            print("Please enter a valid number. Text is not allowed.")
            number(message)

