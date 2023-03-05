from termcolor import colored


def input_error(func) -> str:
    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except KeyError:
            return colored("Wrong format. Please enter: '{command:}{name author}' or {command:}{tag,tag}'", "red")

        except ValueError:
            return colored("You forgot to enter the author name or tags.", "red")

        except IndexError:
            return colored("Can't find information about this author or the data is incorrect.", "red")

        except TypeError:
            return colored("Unknown command or parameters, please try again.", "red")

        except AttributeError:
            return colored("1", "red")

    return inner