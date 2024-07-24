# def modify_number(number):
#
#     if number < 0:
#         number = abs(number)
#
#     return number * 2
#
#
# print(modify_number(5))
# print(modify_number(-3))
# print(modify_number(0))


# def get_unique_numbers(numbers):
#
#     unique_numbers = list(set(numbers))
#     return unique_numbers
#
#
# print(get_unique_numbers([1, 2, 2, 3, 4, 4, 5]))
# print(get_unique_numbers([7, 7, 7, 7, 7]))
# print(get_unique_numbers([1, 2, 3, 4, 5]))


# def authorize_user():
#     name = input("Your name: ")
#     return f"успешно авторизован {name}"
#
#
# authorization_message = authorize_user()
# print(authorization_message)


# def callback(text):
#     print(f"Фиксим баг <{text.strip()}>")
#
#
# def find_a_bug(text: str, callback):
#
#     tasks = text.split(',')
#
#
#     for task in tasks:
#
#         if 'bug' in task.lower():
#             callback(task)
#
#
#
# text = "Done_Task1, Done_Task2, Bug_Task3, Done_Task4, Bug_Task5"
# find_a_bug(text, callback)



# def call_twice(func):
#     def wrapper(*args, **kwargs):
#
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper
#
# @call_twice
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# say_hello("Alice")
#
#
#
#
# def not_negative(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if result < 0:
#             result = abs(result)
#         return result
#     return wrapper
#
#
# @not_negative
# def get_a_number():
#     return -10
#
# @not_negative
# def get_a_number2():
#     return 44
#
#
# print(get_a_number())
# print(get_a_number2())
#
#
#
#
# def not_empty_text(func):
#     def wrapper(text: str, *args, **kwargs):
#         if not text:
#             text = "Hello"
#         return func(text, *args, **kwargs)
#     return wrapper
#
# def to_upper(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
#
#
# @not_empty_text
# @to_upper
# def add_question(text: str):
#     return text + "?"
#
#
# print(add_question(""))
# print(add_question("how are you"))
# print(add_question("good day"))
#
#
#
# def not_negative(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if result < 0:
#             result = abs(result)
#         return result
#     return wrapper
#
#
# @not_negative
# def get_a_number():
#     return -10
#
# @not_negative
# def get_a_number2():
#     return 44
#
#
# print(get_a_number())
# print(get_a_number2())
#
#
#
# def not_empty_text(func):
#     def wrapper(text: str, *args, **kwargs):
#         if not text:
#             text = "Hello"
#         return func(text, *args, **kwargs)
#     return wrapper
#
# def to_upper(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper
#
# @not_empty_text
# @to_upper
# def add_question(text: str):
#     return text + "?"
#
#
# print(add_question(""))
# print(add_question("how are you"))
# print(add_question("good day"))
#



# def repeat(times: int):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator
#
#
# @repeat(3)
# def say_hello(name):
#     print(f"Hello, {name}!")
#
#
# say_hello("Alice")
#
# @repeat(2)
# def add_exclamation(text: str):
#     return text + "!"
#
#
# result = add_exclamation("Hi")
# print(result)
