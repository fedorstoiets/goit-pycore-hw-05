def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        
        if n <= 0:
            return 0

        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(15))  # 610
print(fib(20))  # 6765


import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r"\b\d+\.\d+\b"

    for number in re.findall(pattern, text):
        yield float(number)


def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))


text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими "
    "надходженнями 27.45 і 324.00 доларів."
)

total_income = sum_profit(text, generator_numbers)

print(f"Загальний дохід: {total_income}")



def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    cmd = cmd.lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args

    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]

    if name not in contacts:
        raise KeyError

    return contacts[name]


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."

    result = []

    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")

    return "\n".join(result)


def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            print("Enter a command.")
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()