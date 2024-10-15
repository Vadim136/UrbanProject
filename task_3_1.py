calls = 0


def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()
    lower_string = string.lower()
    for i in list_to_search:
        if i.lower() == lower_string:
            return True
    return False


print(string_info("Hello, World"))
print(string_info("Text to test"))
print(is_contains("Python", ["Hello", "World", "Test", "Python"]))
print(is_contains("Test", ["Hello", "World", "Text", "Python"]))


print(calls)  
