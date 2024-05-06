todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.lower().startswith('add'.casefold()) or user_action.startswith('new'.casefold()):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.lower().startswith('show'.casefold()):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = []

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        new_todos = [item.strip('\n') for item in todos]

        print("\n Todo task list: \n")
        for index, item in enumerate(new_todos):
            print(f"{index + 1}.{item}")
        print("\n")

    elif user_action.lower().startswith('complete'.casefold()):
        try:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                print(f"{index + 1}.{item}")
            print('\n')

            number = int(user_action[9:]) - 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"\nTodo '{todo_to_remove}' was removed from the list!"
            print(message)
        except IndexError:
            print('invalid index.')
            continue

    elif user_action.lower().startswith('edit'.casefold()):
        try:
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                print(f"{index + 1}.{item}")
            print('\n')

            number = int(user_action[5:]) - 1
            new_todo = input("Enter new todo task to replace the old one: ") + '\n'
            todos[number] = new_todo

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("your command is not valid.")
            continue

    elif user_action.lower().startswith('exit'):
        break

    else:
        print("Hey, you! please enter a valid choice!!!")

print("Bye!")
