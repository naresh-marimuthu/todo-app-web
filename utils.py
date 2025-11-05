File_Path = "todos.txt"

def get_todos(filepath=File_Path):
    """reads a file and returns the content"""
    with open(filepath, "r") as file:
        content = file.readlines()
    return content


def write_todo(todos, filepath=File_Path):
    """writes the content to file"""
    with open(filepath, "w") as file:
        file.writelines(todos)


if __name__ == "__main__":
    write_todo(["to yoga and meditation\n", "do cardio\n", "clean the room\n"])
    print(get_todos())
    

    