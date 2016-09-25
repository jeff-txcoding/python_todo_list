todo_list = []

def show_todos():
    """ Show the todo list  """

    print("\nHere is your todo list:\n")

    for todo in todo_list:
        if todo != "DONE":
            print("  * {}".format(todo))


def show_help():
    """ Show the application instructions """

    print("""
Enter your new todo in the prompt:

Enter HELP to show instructions.
Enter SHOW to show current todo list.
Enter DONE to exit the program.
""")


def add_todo(new_todo):
    """ Add a new todo to the list """

    todo_list.append(new_todo)
    print("Added {}, your list contains {} todos.".format(new_todo, len(todo_list)))


def main():
    """ Run the main application """

    show_help()
    
    while True:

        new_todo = input("> ")

        if new_todo == "DONE":
            show_todos()
            break
        elif new_todo == "SHOW":
            show_todos()
            continue
        elif new_todo == "HELP":
            show_help()
            continue
        elif new_todo in todo_list:
            print("{} has already been added to the list!")
            continue
        elif new_todo == "":
            print("The todo can not be blank!")
            continue

        add_todo(new_todo)


main()
