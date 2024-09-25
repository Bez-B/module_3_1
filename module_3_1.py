calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    tuple_1 = (len(string), string.upper(), string.lower())
    return tuple_1


def is_contains(string, list_to_search):
    count_calls()
    low_string = string.lower()
    low_list_to_search = [name.lower() for name in list_to_search]
    if low_string in low_list_to_search:
        return True
    else:
        return False


print(string_info(input("Введите Ваше имя: ")))
print(string_info(input("Введите название Вашего города: ")))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
