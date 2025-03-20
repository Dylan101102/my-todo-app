FILEPATH = "to-dos.txt"


def get_to_dos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        to_dos_local = file_local.readlines()
    return to_dos_local


def write_to_dos(to_dos_arg, filepath=FILEPATH):
    """ Write the to-do items in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(to_dos_arg) # No return statement needed here, action is done after writing to the file.


if __name__ == "__main__":
    print("hi")