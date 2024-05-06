todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter todo task to add: ")
            todos.append(todo)

        case "show":
            print("Todo task list: \n")
            for index, item in enumerate(todos):
                print(f"{index+1}.{item}")
            print("\n")

        case "complete":
            number = int(input("Number of the completed todo task to remove from list: ")) - 1
            todos.pop(number)

        case "exit":
            break

        case "edit":
            number = int(input("Number of the todo task to edit: "))-1
            new_todo = input("Enter new todo task to replace the old one: ")
            todos[number] = new_todo

        case random_string:
            print("Hey, you! please enter a valid choice!!!")

print("Bye!")