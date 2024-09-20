calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(s):
    s = (len(str(s)), str(s).upper(), str(s).lower())
    count_calls()
    return s


def is_contains(s, l):
    s = str(s).lower()
    l = str(list(l)).lower()
    count_calls()
    if s in l:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
