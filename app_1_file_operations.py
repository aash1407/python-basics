todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter todo task to add: ") + "\n"
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case "show":
            file = open("todos.txt")
            todos = file.readlines()
            file.close()

            new_todos = []

            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            new_todos = [item.strip('\n') for item in todos]

            print("Todo task list: \n")
            for index, item in enumerate(new_todos):
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