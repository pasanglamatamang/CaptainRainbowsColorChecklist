checklist = list()


# creates
def create(item):
    checklist.append(item)


# Reads
def read(index):
    return checklist[index]


# updates
def update(index, item):
    checklist[index] = item


# destroys
def destroy(index):
    checklist.pop(index)


# lists the items
def list_all_items():
    index = 0
    for list_items in checklist:
        print(str(index) + list_items)
        index += 1


# Marks completed
def mark_completed(index):
    mark_items = u'\u2713' + checklist[index]
    checklist[index] = mark_items


# Selection
def select(function_code):
    if function_code.upper() == "C":
        input_item = user_input("Input item: ")
        create(input_item)
    elif function_code.upper() == "R":
        item_index = user_input("Index Number? ")
        read(item_index)

    elif function_code.upper() == "P":
        list_all_items()

    elif function_code.upper() == "U":

        update(item_index, input_item)

    elif function_code.upper() == "D":
        item_index = user_input("Index Number? ")
        destroy(item_index)

    elif function_code.upper() == "Q":
        return False

    else:
        print("Unknown Option")
    return True


# user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input


# Tests
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    list_all_items()
    user_value = user_input("Please Enter a value: ")
    print(user_value)


test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to read from list, P to display list, U to update list, D to delete and Q to quit ")
    running = select(selection)
