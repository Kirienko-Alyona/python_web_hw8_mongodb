from termcolor import colored

from search import search_name, search_tag, print_quote

FUNCTIONS = {
    "name": search_name,
    "tag": search_tag,
    "tags": search_tag
}


def handler(input_string: str) -> list:

    command = ""
    data = ""
    input_string = input_string.strip()
    for key in FUNCTIONS:
        if input_string.startswith(key):
            command = key
            data = input_string[len(command):].strip()
            break

    if not command:
        print(colored("I dont know this command", "blue"))

    if data:
        data = data.split(":")
        return FUNCTIONS[command](data[1].strip())

    return FUNCTIONS[command]()


def main():
    while True:
        input_string = input(colored("\nInput words, please: ", "blue"))

        if input_string.lower() == "exit":
            print(colored("Good bye :)", "blue"))
            exit()
        list_quote = handler(input_string)
        for quote in list_quote:
            quote = print_quote(quote)
            print(quote)


if __name__ == '__main__':
    main()
