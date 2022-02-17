"""
Module for JSON file navigation
"""
import json


def read_json(file_name):
    """
    Read json file and return its content
    """
    with open(file_name,"r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def navigate_json(data):
    """
    Work with data from JSON file
    Print items user asks for via input
    """
    if type(data) == list:
        num = len(data)
        print(f"The content is in the list, there are {num} items.")
        if num == 0:
            print("The list if empty. Sorry:)")
            return None
        key = input("Please enter index of item you want to see: ")
        data = data[int(key)]
    elif type(data) == dict:
        list_keys = data.keys()
        print("The content is in the dict.")
        if len(list_keys) == 0:
            print("The dictionary is empty. Sorry:)")
            return None
        print(f"Keys available: {list_keys}")
        key = input("Please enter a key from the above list: ")
        data = data.get(key)
    else:
        print(data)
        return None
    navigate_json(data)


def main():
    """
    Get path to the file from user input
    Call functions
    """
    file_name = input("Please enter a path to JSON file: ")
    data = read_json(file_name)
    try:
        data = read_json(file_name)
    except FileNotFoundError:
        print("File does not exist. Try to restart module and enter a correct path to file.")
        return None
    navigate_json(data)
main()