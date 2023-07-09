#variables that hold constants are written in capital letters and put at the top of the file
FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    """This function is used to get contents in a file.
    its recommended to use doc-strings whenever theres a function"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        todos_local = file_local.writelines(todos_arg)
    return todos_local

#only print hello if its used directly for this function not in main code where its called
if __name__ == "__main__":
    print("Hello")