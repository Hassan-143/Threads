import threading
import string

input_string = ""


def input_thread():
    try:
        global input_string
        input_string = input("\nPlease enter a string: ")
        print("\nThe input string is:", input_string)

    except EOFError:
        print("Input thread is terminated.")


def reverse_thread():
    global input_string
    reversed_string = input_string[::-1]
    print("The reversed string is:", reversed_string)


def capital_thread():
    global input_string
    capital_string = input_string.upper()
    print("The capitalized string is:", capital_string)


def shift_thread():
    global input_string
    shift_string = ""

    for char in input_string:
        # To check if the character is a letter or a lowercase.
        if char.isalpha() and char.islower():
            shift_string += chr(ord(char) + 2)
        else:
            shift_string += char
    print("The shifted string is:", shift_string)


if __name__ == '__main__':
    thread1 = threading.Thread(target=input_thread)
    thread2 = threading.Thread(target=reverse_thread)
    thread3 = threading.Thread(target=capital_thread)
    thread4 = threading.Thread(target=shift_thread)

    thread1.start()
    thread1.join()

    thread2.start()
    thread3.start()
    thread4.start()

    thread2.join()
    thread3.join()
    thread4.join()
