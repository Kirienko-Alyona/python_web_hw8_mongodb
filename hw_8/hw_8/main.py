from termcolor import colored
# def exit_func(*_) -> str:
#     """The function close bot."""
#     return exit(colored("Bye! I'm gonna miss you ;)\n", "blue", attrs=["bold"]))
FUNCTIONS = {
    "name:": get_name(),
    "tag": get_tag(),
    "tags:": get_tags()
}

def handler(input_string: str) -> list:
  
    command = ""
    data = ""
    input_string = input_string.strip().lower() + " "
    for key in FUNCTIONS:
        if input_string.startswith(key + " "):
            command = key
            data = input_string[len(command):].strip()
            break

    if not command:
        print(colored("I dont know this command", "blue"))

    if data:
        args = data.strip().split(" ")
        return FUNCTIONS[command](args)

    return FUNCTIONS[command]()



def main():
    while True:
        input_string = input("\nInput words, please: ")

        if input_string.lower() == "exit":
            #exit_func()
            print(colored("Good bye :)", "blue"))
            exit()
        print(handler(input_string))






if __name__ == '__main__':
    main()