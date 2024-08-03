
def data_get():
    first_name = input('enter first_name: ')
    last_name = input('enter last_name: ')
    DOB = input('enter DOB(date of birthday): ')
    social = input('enter social security: ')
    return first_name, last_name, DOB, social


def value_key_system(first_name: str, last_name: str, DOB: str, social: str) -> str:
    data = ['First_name=', first_name, "Last_name=", last_name, 'DOB=', DOB, 'social_security=', social]
    result = ''.join(data)
    return result


def separator_semicolon(first_name: str, last_name: str, DOB: str, social: str) -> str:
    data = [first_name, ';', last_name, ';', DOB, ';', social]
    result = ''.join(data)
    return result


def separator_space(first_name: str, last_name: str, DOB: str, social: str) -> str:
    data = []
    while len(first_name) < 9:
        first_name += ' '
    data.append(first_name)
    while len(last_name) < 10:
        last_name += ' '
    data.append(last_name)
    while len(DOB) < 11:
        DOB += ' '
    data.append(DOB)
    while len(social) < 12:
        social += ' '
    data.append(social)
    result = ''.join(data)
    return result


if __name__ == "__main__":
    first_name, last_name, DOB, social = data_get()
    number_one = value_key_system(first_name, last_name, DOB, social)
    print(number_one)
    number_two = separator_semicolon(first_name, last_name, DOB, social)
    print(number_two)
    user_input = (first_name, last_name, DOB, social)
    number_three = separator_space(first_name, last_name, DOB, social)
    print(number_three)


