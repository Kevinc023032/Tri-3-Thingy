from week0 import swap, christmastree, ship
from week1 import lists

import tt0_1

main_menu = []

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Ship Animation", ship.ship],
    ["Christmas Tree", christmastree.driver],
]

list_sub_menu = [
    ["For Loop", lists.for_loop],
]

math_sub_menu = [
    ["Swap", swap.swap],
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def list_submenuc
# using list_sub_menu list:
# list_submenuc works similarly to menuc
def list_submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, list_sub_menu)
    m.menu()


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Fun", submenu])
    menu_list.append(["Data", list_submenu])
    menu_list.append(["Math", math_submenu])
    buildMenu(title, menu_list)

# def submenu
# using sub menu list above:
# sub_menu works similarly to menu()
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
def list_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, list_sub_menu)
def math_submenu():
    title = "Function Submenu" + banner
    buildMenu(title, math_sub_menu)

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()