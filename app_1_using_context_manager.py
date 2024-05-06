todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter todo task to add: ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = []

            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            new_todos = [item.strip('\n') for item in todos]

            print("Todo task list: \n")
            for index, item in enumerate(new_todos):
                print(f"{index + 1}.{item}")
            print("\n")

        case "complete":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                print(f"{index + 1}.{item}")
            print('\n')

            number = int(input("Enter the number of the completed todo task to remove from the list above: ")) - 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"\nTodo '{todo_to_remove}' was removed from the list!"
            print(message)
        case "exit":
            break

        case "edit":
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                print(f"{index + 1}.{item}")
            print('\n')

            number = int(input("Enter the number of the todo task to edit from the above list: ")) - 1
            new_todo = input("Enter new todo task to replace the old one: ") + '\n'
            todos[number] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case random_string:
            print("Hey, you! please enter a valid choice!!!")

print("Bye!")
