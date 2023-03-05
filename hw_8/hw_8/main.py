import re
import chardet
from termcolor import colored
from decor import input_error

from search import search_name, search_tag, return_quote

FUNCTIONS = {
    "name": search_name,
    "tags": search_tag,
    "tag": search_tag
}


@input_error
def handler(input_string: str) -> list:

    command = ""
    data = ""
    input_string = input_string.strip()
    for key in FUNCTIONS:
        if input_string.startswith(key):
            command = key
            data = input_string[len(command):].strip().split(":")
            data = data[1].strip().split(",")
            break
    if data[0] !='':
        if len(data) != 0:
            return FUNCTIONS[command](data)
    else:
        raise ValueError


def main():
    while True:
        input_string = input(colored("\nInput words, please: ", "blue"))

        if input_string.lower() == "exit":
            print(colored("Good bye :)", "blue"))
            exit()
            
        list_quote = handler(input_string)
        
        if not (isinstance(list_quote, str)):
            for quote in list_quote:
                quote = return_quote(quote)
                print(quote)
        
        else:       
            print(list_quote)

if __name__ == '__main__':
    main()
